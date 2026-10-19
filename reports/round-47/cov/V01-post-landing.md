# V01 — post-landing verification of the cartography landing (claim C)

- Seat: V01 | role: verifier | claim: C | out: `reports/round-47/cov/V01-post-landing.md`
- Measurement window: 2026-10-19, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- HEAD at measurement: `6e9a30d` (`git rev-parse --short HEAD`)
- Mission: after the integrator applies C, re-run the partition census + absence sweep +
  index sweep; confirm total 224 and no second owner.

**Verdict: `PRE-LANDING / could-not-evaluate` on live bytes — staged 224 proof GREEN.**
The C landing is not present at HEAD `6e9a30d`: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`
does not exist, `corpus/` is clean, and `reports/round-47/cov/` was empty when I began. (C
seats filed drafts while this seat worked; those are cross-checked read-only in §3.1.)
A "post-landing PASS" on real bytes is therefore not available to this seat, and claiming one
would be theater. What is measured below: the live 223 baseline, an independent freshness
re-confirmation, and a scratch-only staged landing that exercises every post-landing
arithmetic and ownership assertion. The live verdict remains owed and is specified as an
executable block in §7; the claim's `after_required` stays unproven until that block runs
against the integrator's actual bytes.

---

## 1. Live baseline (measured, not asserted)

```
$ git rev-parse --short HEAD
6e9a30d
$ git status --porcelain corpus/
                                        # empty
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

The round-28 index sweep against the live tree (`reports/round-28/readme/sweep.py`, read-only)
is green:

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

The independent inventory agrees: `tools/source-audit-inventory.py --json --summary --root
corpus/knowledge` → `"files": 223`.

Landing shape pre-check (the "A not M" condition):

```
$ git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path '...' does not exist in 'HEAD'
exit=128
$ git ls-tree HEAD corpus/knowledge/culture-material/ | grep -c cartography
0
$ git diff --stat HEAD -- corpus/knowledge
                                        # empty
```

So the proposed path is absent at HEAD and would land as a **new path**, not an overwrite.
`corpus/README.md` is the only existing corpus file the claim authorizes changing.

---

## 2. Freshness re-confirmed at the live 223 (independent of K02)

**Filename test.** `find corpus/knowledge -type f \( -iname '*map*' -o -iname '*chart*' -o
-iname '*atlas*' -o -iname '*survey*' -o -iname '*cartograph*' -o -iname '*portolan*' -o
-iname '*cadastr*' -o -iname '*itinerar*' \)` returns two files, both false positives:

| File | Why not an owner |
|---|---|
| `myth-symbol/sacred-kingship-mythic-charter.md` | substring `chart` inside "charter" |
| `synthesis/dialect-faction-map-workflow.md` | "Map" is a **verb** — mapping dialect features onto networks (`:2`) |

Explicit cartography-family filenames (`*cartograph*`, `*mapmaking*`, `*portolan*`,
`*cadastr*`): **0**.

**Topic test, full topic block (not just the first line).** I extracted each entry's complete
`- topic:` block with the sweep's own `TOPIC_RE` (`reports/round-28/readme/sweep.py:61`) and
matched map vocabulary. Live 223 → **14 full-topic hits**, all metaphor, verb, statistical
"survey", or handoff; explicit cartography-family topic owners: **0**.

- Metaphor: `sound-symbolism` (three-way map), `dialect-register-consistency` (dialect map),
  `purity-pollution-boundary-systems` (boundary map), `ritual-garments` (atonement map),
  `finnic-sami` (identity map), `mesoamerica-primary-sources` (reference map),
  `africa-primary-sources` (source map), `sociolinguistics-registers` (register maps to),
  `animal-symbolism` (fauna maps to land).
- Verb: `dialect-faction-map-workflow:2` ("Map dialect features … onto travel networks").
- Statistical: `number-symbolism:3` ("a variance survey").
- Adjacent/handoff: `sacred-topography-pilgrimage:5` ("sacred-geography mapping … as a
  diagram" — the nearest neighbour), `sacred-registers-liturgical-language:3` (ritual events
  map to competences), `contact-strata-verification-gate:3` (mapping a packet).

**Prior-round non-carriage.** `grep -rlniE '(cartograph|mapmak|portolan|cadastr)' reports/
--include='*.md'` returns 14 paths: eight under `reports/round-44/` (the K02 seed and its
downstream collision/scope/review/integration artifacts) and six frozen scratch copies of
`mesoamerica-primary-sources.md` under `reports/supplement-opencode-1/`. **No path under
`reports/round-1..43/` names cartography as a gap or proposal.** The topic is not carried as
of `6e9a30d`; it must be re-checked at the actual landing (§7), because freshness is a
landing-time property, not a one-time scout result.

---

## 3. Staged 224 landing (scratch-only proof)

Because the integrator has not applied C, I staged the landing under `.scratch/v01/stage/`
(never under `corpus/`) and measured it:

1. Mirror `corpus/knowledge` → `.scratch/v01/stage/knowledge` (223 files).
2. Add a **fixture** entry at `culture-material/cartography-and-mapmaking.md`. The fixture is
   K02's topic seed plus the minimal head block; it is deliberately **not the C entry body**
   and is not a proposal for the landing text. Its only job is to exercise the index
   mechanics (`- topic:` byte-equality, counts, footer).
3. Apply the mechanical README rev-2.5 edits to a copy: new revision block, section header
   25→26, row inserted in filename order, totals 223→224, footer total/vector, and the
   rev-2.4 prose-vector repair.
4. Run the sweep by importing the module and calling
   `sweep(readme_text, root_override=stage/knowledge)`. The CLI has no `--root` flag
   (`reports/round-28/readme/sweep.py:411-421`); the module-level `sweep()` exposes the
   override used by its own selftest (`:119-121`).
5. Run the independent inventory with `--root .scratch/v01/stage/knowledge`.

Measured result:

```
parts (README order) linguistics 25, myth-symbol 26, culture-material 26,
                     synthesis 29, verification 24, civilizations 94
rows 224 files 224
missing_from_index []   topic_mismatch []   orphan_rows []   header_drift {}
totals_line 224 totals_ok True
footer {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_findings [] footer_ok True
sweep.ok True
inventory files 224
```

| Post-landing assertion | Staged measurement |
|---|---|
| total | 224 == 224 |
| culture-material | 26 |
| rows vs files | 224 == 224, 0 missing, 0 ghosts, 0 duplicates |
| topic equality | 0 mismatches (README row byte-equal to fixture `- topic:`) |
| header drift | `{}` (declared counts equal live counts in all six sections) |
| totals line | 224 |
| footer total / vector | 224 / `25/26/26/29/24/94` |
| footer findings | `[]` |
| independent inventory | `"files": 224` |
| existing entries overwritten | **0** — all 223 mirrored files byte-identical by SHA-256 |
| filename owners of cartography | 1 (the new fixture only) |
| topic owners of cartography | 1 (the new fixture only) |
| row order | sorted ascending; inserted line 243, between `calendar-festival-systems.md` (242) and `costume-semiotics.md` (244) |

Fixtures, for reproducibility only (not landing pins; the real draft will differ):

- fixture entry: `cb828b2524adf895bbf0d8b2974a3f6242db86ff9e2d8ae9ae9873259a6395d9`, 2604 bytes
- staged README: `b150f0926fa58d113f2984d32cbaecc41011086bbce227158b53ea3416ff38f5`
- live README: `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`

In my mirror, the staged README differs from live in exactly **3 diff hunks** — the revision
block (+2 lines), the culture-material header and its one inserted row, and the totals/footer
lines. No other README line changes. The sweep's own selftest remains 12/12 green.

### 3.1 Cross-check against the C drafts filed after my first measurement

Several C seats filed while this seat worked. Read-only checks against their artifacts:

- `reports/round-47/cov/C04-entry-header.md:114` files the head block. Its `- topic:` is 766
  chars, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495`, byte-equal
  to K02's seed (`reports/round-44/scout/K02-gap-scout.md:227`) and to C09's README row.
- `reports/round-47/cov/C09-readme.md` files a fenced README diff and a post-edit README at
  `.scratch/c09/README.post.md` (sha256 `73985f68e48cbc7015eb00b1080796a5b93632eeb9b7ad76290074bf8de95afc`).
  Swept against C09's own `tree224` (224 files; cartography fixture carrying the same
  766-char topic): rows 224 == files 224, culture-material 26, footer 224 /
  `25/26/26/29/24/94`, 0 missing, 0 topic mismatches, `ok: true`. Its rev-2.5 target vector is
  `25/26/26/29/24/94`; its repaired rev-2.4 target is `25/26/25/29/24/94`. Its four-hunk
  normalized diff passes `git apply --check` against the live tree (exit 0).
- `reports/round-47/cov/C10-sweep.md` files an independent staged tree
  (`.scratch/r47-c10/README.staged.md`, sha256
  `0ab794d8acb7e61cfd0f408b28a257f287431334a452d36af735ec2e46b7f95d`; fixture sha256
  `9e47f3a0bcf0253f6f9d8c52956fc755d449d994d4b1f8f75437d5440df23826`): same 224/26/footer
  result, `ok: true`.
- My mirror (§3) agrees on every measurement field. Three independent stagings converge. The
  differing README shas (mine `b150f0…`, C09 `73985f…`, C10 `0ab794…`) differ only in
  revision prose and fixture bytes; none is a landing pin.

**Hazard found (scratch, not a filed defect):** `.scratch/c09/entry.md` (61,411 bytes) is a
stale **round-35 death-and-afterlife** artifact — its `- topic:` is 1,948 chars, sha256
`feb8fa7254c5919dc5ff2a38ff40c0aa156d939ef54987738d1655b6b190cb2a`, and its head names
`death-afterlife-eschatology`. Pairing it with C09's README produces exactly one
`topic_mismatch` (class `REWRITE`), not a count error. The integrator must assemble the
cartography entry from C04's head block plus the C01-C03 body fragments, **not** lift
`.scratch/c09/entry.md`; the live sweep will surface a wrong lift as a topic mismatch, not a
green.

---

## 4. No second owner

Zero other entries own the register. The nearest neighbours and their binding boundaries:

| Neighbour | What it owns (live citation) | Boundary status |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | five world-model axes; T-O diagram as symbolic device. `:71` — "T-O diagrams are symbolic, not survey maps (§10)"; `:102` — "T-O diagrams are symbolic devices, not cartographic claims." | Explicit disclaimer of the survey-map register. Nearest overlap is terminological ("cosmographic" as a map form); the draft must cite `:71`/`:102` and must not restate the five-axis typology. |
| `myth-symbol/sacred-topography-pilgrimage.md` | the place register and the route as rite (`:5`) | Owns holy sites/route; the new entry owns how a route is measured and drawn. The route types are map *content*, not a second ownership. |
| `myth-symbol/direction-symbolism.md` | orientation frames, cardinal coinage, the true-vs-magnetic "compass trap" (`:51`) | Owns the direction register; the new entry owns the map convention (rose, north arrow) and cites `:51`. |
| `culture-material/architecture-settlement-lexicon.md` | the built-environment lexicon; castrum grid surveyed with the groma, "the grid is cadastral" (`:95`) | Owns the city plan. The sentence names the survey step as a handoff; the new entry must cite `:95`, not restate settlement vocabulary. "Cadastral" here is the closest lexical overlap and is a drafting risk. |
| `culture-material/writing-media-surface-economy.md` | seven surface families and the cost ladder (`:3`) | Owns surfaces; the new entry owns map-specific media/reproduction (parchment, cloth, copperplate, atlas). |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo/cartographic-history **source class** and provenance (`:58`) | Owns the manuscript inventory; the new entry cites the genre. |
| `culture-material/transport-mobility-lexicon.md` | routes, maintenance, mobility layers (`:28`) | Owns route maintenance; the new entry owns the representation of routes. |

Verdict at staged 224: **no second owner**. The fixture's `- couples:` targets all resolve at
HEAD (7/7 checked by `test -f`), so the ownership question is not hiding a dangling reference.
Residual drafting obligations for C06/C07/R03: (a) cite the cosmography disclaimer rather
than absorbing it; (b) cite `architecture-settlement-lexicon.md:95` for the cadastral/groma
handoff; (c) keep the new entry's "cosmographic" map form distinct from the world-model
typology.

---

## 5. README arithmetic and the rev-2.4 prose defect

Live defect, `corpus/README.md:11`:

```
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
```

The arithmetic, computed (not eyeballed):

| Vector | Sum | Reading |
|---|---|---|
| `25/23/25/29/24/94` | 220 | pre-2.4 vector, matches rev 2.3's total 220 |
| `25/23/26/25/24/94` | **217** | the rev-2.4 prose target — defective: the myth-symbol +3 is placed in the culture-material slot and synthesis is cut 29→25 |
| `25/26/25/29/24/94` | 223 | correct post-2.4 vector |
| `25/26/26/29/24/94` | 224 | required post-2.5 vector |

The staged rev-2.5 edit moves `223 → 224` with `25/26/25/29/24/94 → 25/26/26/29/24/94`
(sum 223 → 224) and repairs the rev-2.4 line to `25/26/25/29/24/94` (sum 223). Staged diff
touches only: `:5` (rev-2.5 block), `:236` header 25→26, `:243` the new row, `:547` totals
223→224, `:549-551` footer total and vector.

**Instrument finding (operability, reported not fixed).** `reports/round-28/readme/sweep.py`
does not check README row *order*, and it does not sum prose vectors — it reads the structured
`## part/ (N)` headers, rows, totals line and dated footer (`:59-60`, `:85-150`, `:106-117`).
That is why the rev-2.4 prose defect survived a green sweep. My staged check adds both legs
(row sortedness; defect-vector absence and rev-2.5 sum). This is not in claim O's scope and I
changed no instrument; it is a candidate defect for a later round.

---

## 6. What this certifies — and what it does not

Certified by measurement:

- live pre-state: 223 total, culture-material 25, sweep green 223==223, corpus clean;
- the target path is absent at HEAD and would be an addition, not an overwrite;
- the gap is still unowned at `6e9a30d` and is not carried from `reports/round-1..43/`;
- a mechanically correct 224 landing sweeps green, preserves all 223 existing entry bytes,
  and creates exactly one owner;
- the README arithmetic including the rev-2.4 repair sums correctly;
- the filed C drafts agree on the topic and the arithmetic: C04's header topic == C09's
  README row == K02's seed (766 chars, sha256 `bc7274f4…`), and C09's own `tree224` plus
  C10's independent staged tree both sweep green at 224 with footer `25/26/26/29/24/94`
  (§3.1).

**Not certified (owed):** the real entry's content, source honesty and QUALITY contract
(C06/C07/R03); the actual post-landing bytes; the integrator's exact rev-2.5 prose. The live
post-landing verdict is `could-not-evaluate` until §7 runs. I edited no corpus file, no
`reports/round-1..46/**` byte, and no instrument; the staging tree is disposable `.scratch`.

---

## 7. Post-landing re-run block (integrator, after applying C)

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Every
line is an assertion with the expected value; any failure is a landing defect, not a warning.

```bash
# 1. partition census
test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 224
test "$(ls corpus/knowledge/culture-material/*.md | wc -l)" -eq 26
for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
  printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"
done   # expect 94 / 26 / 25 / 26 / 29 / 24

# 2. the claim's counting command — must be run live, not against a mirror
python3 -B reports/round-28/readme/sweep.py; echo "sweep_exit=$?"
# expect: rows 224 files 224; 0 missing; 0 topic_mismatch; 0 ghosts; {} drift;
#         totals_line 224; footer 224 and 25/26/26/29/24/94; exit 0

# 3. independent inventory
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge \
  | grep -o '"files": [0-9]*'   # expect "files": 224

# 4. landing shape: new path untracked, README modified, nothing else
#    (assumes the round's no-commit rule; if the integrator committed the landing,
#     replace the cat-file line with `git log --diff-filter=A --oneline -- <path>`,
#     which must show exactly one addition)
git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md 2>/dev/null
test $? -eq 128                      # absent at HEAD -> addition, not modification
git status --porcelain corpus/       # expect exactly:
                                     #  M corpus/README.md
                                     # ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
test -z "$(git diff --name-only HEAD -- corpus/knowledge)"   # no existing entry touched

# 5. ownership: exactly one filename owner and one explicit topic owner
test "$(find corpus/knowledge -type f \( -iname '*cartograph*' -o -iname '*mapmaking*' \
  -o -iname '*portolan*' -o -iname '*cadastr*' \) | wc -l)" -eq 1
test "$(grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l)" -eq 1

# 5b. freshness at landing: no pre-r44 proposal (the r44 K02 seed is the source, not a carrier)
test -z "$(grep -rlniE '(cartograph|mapmak|portolan|cadastr)' reports/round-{1..43} --include='*.md' 2>/dev/null)"

# 6. row order, topic byte-equality, prose vectors
python3 -B - <<'PY'
import re, sys
sys.path.insert(0, 'reports/round-28/readme')
import sweep
text = open('corpus/README.md', encoding='utf-8').read()
rows = [f for f, _ in sweep.parse_readme(text)['culture-material']['rows']]
assert rows == sorted(rows), 'culture-material rows not in filename order'
assert rows.count('cartography-and-mapmaking.md') == 1
assert '→ **25/23/26/25/24/94**' not in text, 'rev-2.4 defect left as a target vector'
rev25 = text[text.index('revision: 2.5'):text.index('revision: 2.4')]
vecs = re.findall(r'\*\*(\d+(?:/\d+){5})\*\*', rev25)
assert vecs and sum(map(int, vecs[-1].split('/'))) == 224, vecs
assert vecs[-1] == '25/26/26/29/24/94', vecs
rev24 = text[text.index('revision: 2.4'):text.index('revision: 2.3')]
v24 = re.findall(r'→ \*\*(\d+(?:/\d+){5})\*\*', rev24)
assert v24 and sum(map(int, v24[-1].split('/'))) == 223, v24
print('row order OK; rev2.5 target', vecs[-1], '= 224; rev2.4 target', v24[-1], '= 223')
PY

# 7. second-owner check over full topic blocks (catches continuation lines)
python3 -B - <<'PY'
import os, re, sys
sys.path.insert(0, 'reports/round-28/readme')
import sweep
pat = re.compile(r'(cartograph|mapmak|portolan|cadastr|survey map)', re.I)
owners = []
for part in sweep.PARTS:
    d = os.path.join('corpus/knowledge', part)
    for name in sorted(os.listdir(d)):
        if not name.endswith('.md'):
            continue
        m = sweep.TOPIC_RE.search(open(os.path.join(d, name), encoding='utf-8').read())
        topic = ' '.join(ln.strip() for ln in m.group(1).splitlines()) if m else ''
        if pat.search(topic):
            owners.append(f'{part}/{name}')
assert owners == ['culture-material/cartography-and-mapmaking.md'], owners
print('single topic owner:', owners[0])
PY
```

Expected final state: 224 entries, culture-material 26, sweep green `224 == 224`, footer
`25/26/26/29/24/94`, exactly two corpus paths changed (the new entry and `corpus/README.md`),
one cartography owner.

If any assertion fails, report the measured value and the failing command; do not restate the
claim as passed. A 224 total with a non-224 footer, a second topic owner, or any third changed
corpus path is a landing defect.

---

## 8. Owed / to-verify

- **Live post-landing verdict: owed.** Only the integrator can run §7 against real bytes.
  Until then the claim's `after_required` is unproven; this seat's status is
  `staged-green / live could-not-evaluate`.
- **C draft's real `- topic:` text: assembled entry still to-verify.** C04's filed header and
  C09's README row already agree byte-for-byte (766 chars, sha256 `bc7274f4…`), but the
  integrator's assembled entry must carry that same block; the sweep's `topic_mismatch` leg is
  the check, and the staged fixture's topic is not binding. Do not lift `.scratch/c09/entry.md`
  — it is a stale round-35 death-and-afterlife artifact (§3.1).
- **rev-2.5 prose wording: C09/integrator's.** Only the numeric assertions bind: target vector
  `25/26/26/29/24/94` (sum 224), no surviving `25/23/26/25/24/94`.
- **`reports/round-47/run-validation.py`: absent at my window** (`ls` → No such file or
  directory), though `claims.json` cites it for O/Ca. Not this claim; the integrator should
  not treat its absence as a V01 failure.
- **Staged shas are fixture-dependent** and must not be pinned as the landing. The real
  landing pins should be computed from the integrator's bytes.
- **No collisions found.** `git cat-file -e` exit 128 and `ls-tree` count 0 prove the slug is
  unused; the only filename false positives are `dialect-faction-map-workflow.md` ("map" as
  verb) and `sacred-kingship-mythic-charter.md` (substring "chart").

---

## Appendix — command transcript (key lines)

```text
$ git rev-parse --short HEAD
6e9a30d
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223 ... totals_line 223 totals_ok True ... footer_ok True ... exit=0
$ git status --porcelain corpus/
                                        (empty)
$ git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md
exit=128
$ git ls-tree HEAD corpus/knowledge/culture-material/ | grep -c cartography
0

# staged 224 (scratch mirror, sweep imported with root_override)
parts: civilizations 94, culture-material 26, linguistics 25, myth-symbol 26, synthesis 29, verification 24
rows 224 files 224; missing [] topic_mismatch [] orphan_rows [] drift {}; totals_line 224
footer 224 / [25, 26, 26, 29, 24, 94]; footer_findings []; ok True
inventory files 224
originals changed []  (223/223 byte-identical)
filename owners 1; topic owners 1; row_order_ok True; row position 6 (index 5)
diff live vs staged README: 3 hunks only

# arithmetic
25/23/25/29/24/94 = 220
25/23/26/25/24/94 = 217   (rev-2.4 defect)
25/26/25/29/24/94 = 223   (correct post-2.4)
25/26/26/29/24/94 = 224   (required post-2.5)
```
