# W02 — C landing spec: exact apply instructions for the cartography entry + README rev 2.5

- Seat: `W02` | role: executor | claim: **C** | date 2026-10-19
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), equal to
  `reports/round-47/claims.json:7`
- Out path: `reports/round-47/cov/W02-landing-spec.md` (this file; the only path this seat wrote)
- Mission (`reports/round-47/targets.json`, seat W02): wire the C landing — target path, byte
  source, README rev 2.5 edit — as exact integrator instructions
- Status: **APPLY SHEET, NOT AN APPLIED LANDING.** Nothing under `corpus/` was written or staged.
  All byte sources below are fenced drafts or assembler output in `.scratch/w02/`.

## 0. Bottom line

The C landing is **mechanically ready and end-to-end measured green** on a staged 224 tree:
one added entry, README rev 2.5, `rows 224 files 224`, footer `25/26/26/29/24/94`, exit 0.
The landable byte source is **not** the raw concatenation of the four fenced fragments as filed: the raw
bytes still carry the C08 P1 boundary/citation defects and the R02 C-D2/C-D3 defects. The
assembler in §3.5 applies those corrections and pins the result at
`8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b` (797 lines, 130,776 bytes).

**One gate is not closed by this sheet: length (C-D1).** 797 lines is 3.6× the live partition
maximum (221) and 2.3× P02's 340-line bloat line. On the pre-landing bytes, C07's executable
check calls it a WARN and returns 0 FAIL, but C11 §5 D1 calls it blocking and R02/X04
condition 5 says coverage is
`unchanged` on quality if the entry lands undeduplicated. The integrator must choose one of:

1. **Trim/dedupe to ≤340 lines** (P02 bloat line; C07 band is ≤260), then re-run §5–§6 with a
   new byte pin; or
2. **File an explicit C07/R03 waiver** naming the length exception (R03's fragment
   `reports/round-47/review/R03-c-content.md` is absent at spec time, so C07's author or the
   parent must file it); or
3. **Land at 797 and record the C axis as `unchanged`** (count moved, quality flat), not
   `improved`.

Do not land silently at 797 and claim `improved`. The arithmetic is safe; the quality verdict
is not.

## 1. Target and landing type

| item | value | evidence |
|---|---|---|
| target path | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | absent at spec time (`ls` → No such file) |
| landing type | **A** (add), never **M** (modify) | target absent; `git status --porcelain` shows no tracked corpus change |
| slug sort slot | between `calendar-festival-systems.md` (5) and `costume-semiotics.md` (6) | `ls corpus/knowledge/culture-material/ \| nl` |
| pre-landing total | **223** files; culture-material **25** | `find corpus/knowledge -name '*.md' \| wc -l` → 223; `ls corpus/knowledge/culture-material/*.md \| wc -l` → 25 |
| pre-landing vector | `25/26/25/29/24/94` (linguistics / myth-symbol / culture-material / synthesis / verification / civilizations) | `python3 -B reports/round-28/readme/sweep.py` → footer_live |
| post-landing total | **224**; culture-material **26** | staged §4.3 |
| post-landing vector | `25/26/26/29/24/94` = **224** | arithmetic; confirmed by sweep parts |

The claim's `after_required` is `reports/round-47/claims.json:28`: entry landed per the entry
contract; total 224; culture-material 26; README rev 2.5 sweep-green 224==224; prose vector
sums 224; audits PASS; zero overwrites; gap re-verified unowned at landing.

## 2. Preflight receipt (measured at spec time, 2026-10-19)

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| check | command | measured | expected |
|---|---|---|---|
| HEAD | `git rev-parse HEAD` | `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` | baseline |
| total | `find corpus/knowledge -name '*.md' \| wc -l` | `223` | 223 |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | `25` | 25 |
| target free | `test ! -e corpus/knowledge/culture-material/cartography-and-mapmaking.md` | true | absent |
| filename probe | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | `0` | 0 |
| topic-owner probe | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr)' corpus/knowledge/ \| wc -l` | `0` | 0 |
| live sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, exit 0 | green |
| README sha | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | pin |
| README rev | `grep -n '^revision:' corpus/README.md` | `2.4` at `:5` | 2.4 |
| README totals | `grep -n '^Total knowledge entries' corpus/README.md` | `:544` = 223 | 223 |
| README footer | `grep -n 'directory totals' corpus/README.md` | `:548` = `25/26/25/29/24/94` | 223 |
| rev-2.4 prose defect | `sed -n '11p' corpus/README.md` | `25/23/26/25/24/94` = **217** | 217 (defect) |
| README diff applies (after §4.2 extraction) | `git apply --check .scratch/w02/readme-rev25.diff` | exit **0** | 0 |
| worktree | `git status --porcelain` | only `?? reports/round-46/review/`, `?? reports/round-47/` | no tracked corpus change |

The rev-2.4 prose vector is a one-position slip plus a dropped value: myth-symbol's new `26`
was written into the culture-material slot, the old culture-material `25` was pushed into the
synthesis slot, and synthesis's `29` disappeared; slot 2 stayed `23` (`25+23+26+25+24+94 =
217`). The live footer already reads the correct `25/26/25/29/24/94` = 223, which is why green
sweeps never caught the prose defect — the sweep reads the totals line and footer
(`reports/round-28/readme/sweep.py:106-116,160-161`), not revision-block prose.

## 3. Byte source and pins

### 3.1 Fragment pins

Assembly order is **C04 head + C01 §§1–4 + C02 §§5–9 + C03 §§10–15**, each lifted from its
`markdown`-labelled fenced block. C03 uses a four-backtick fence; the others use three.

| seat | fragment path | file sha256 | fenced block sha256 | block lines | block chars |
|---|---|---|---|---|---|
| C04 | `reports/round-47/cov/C04-entry-header.md` | `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` | `962842fa53cf0215b6cc62fb6b524f202140ec2bf5bf7247fb14b268bc55118b` | 51 | 20,945 |
| C01 | `reports/round-47/cov/C01-entry-a.md` | `cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d` | `a44fc4cceda5e7787130ca8b65a6e69b3b58eac5fecb72ec82e817a04fb866db` | 201 | 32,354 |
| C02 | `reports/round-47/cov/C02-entry-b.md` | `5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af` | `abc203c35038d6dd3e2e3a256d8bfa10d2d731a466e16648c69ae80167377f8c` | 361 | 44,527 |
| C03 | `reports/round-47/cov/C03-entry-c.md` | `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` | `d2939957467adc2f300cbe9313fb42bfb38489e95223850e576b18179555e89c` | 177 | 30,117 |

Blocks are joined with **one blank line** between fragments and a single trailing newline: the
head block's last field (`- scope:`) needs a blank line before `## 1.`, matching the live
convention (`corpus/knowledge/culture-material/timekeeping-instruments.md:1-13`).

### 3.2 Raw assembly — pin, but do not land

| measurement | value |
|---|---|
| path in scratch | `.scratch/w02/assembled.md` (regenerable; not a deliverable) |
| lines / bytes | **793** / **128,673** |
| sha256 | `50c854713fcb1b242176f896431232fdcd9ad88fa9101374d4d02d824be93f55` |
| C07 check | 0 FAIL, 2 WARN (README row absent; length 793) |
| known defects it still carries | C08 P1-2 (ladder `:44`), P1-3 (no trade row), P1-4 (no celestial row), P2-1 (craft/sacred only in seat-side notes); R02 C-D2 (`cosmology:27` undisposed); R02 C-D3 (`cartograph` count "3 lines") |

**C11's pin is stale.** `reports/round-47/cov/C11-scribe.md:43-46` records **854 lines / 800
body / 132,075 bytes / `bc12037c38f4472a5e8e7435fde95a98d3fa8f1c8305881b49f263384c1fc892`**.
That measurement predates C02's 15:10 revision, which cut the C02 fenced block from 424 to 361
lines. Re-running the same assembly against the live fragments yields 793 lines and
`50c85471…`; C11's `bc12037c…` must not be used as a landing pin.

### 3.3 Landable assembly — the byte source

| measurement | value |
|---|---|
| output | `.scratch/w02/landable.md` |
| lines / bytes | **797** / **130,776** |
| sha256 | `8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b` |
| `- topic:` | 766 chars, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495`, byte-equal to the r44 seed line `reports/round-44/scout/K02-gap-scout.md:227` |
| README row derived from it | 801 chars, sha256 `2ff3050862ed6b8487e8bbb69e6e214eaa6936731570ad74e01a429ffd6d9e2c`, byte-equal to C09's `+` row |
| head fields | 8, in order: `topic > gap filled > sources > source > couples > verified-at > recheck > scope` |
| `- couples:` | one physical line, 4,566 chars, **23 unique tokens, 23/23 resolve** from `corpus/knowledge/culture-material/` (C13's 21/21 is superseded by the two added tokens) |
| sections | 1–15, each exactly once, in order; one H1 |
| C07 check | **0 FAIL, 2 WARN** (README row absent → PASS after §4; length 797) |

### 3.4 Correction ledger (each sourced; no ungrounded content)

| # | correction | authority | old → new |
|---|---|---|---|
| 1 | `cartograph` probe/count | R02 C-D3 (`review/R02-review.md:127`), X04 §4 (`cross/X04-coverage-critic.md:114`) | "`grep -rli 'cartograph'` → 2 files / 3 lines" → "`grep -rli` → **2 files**; `grep -rn` → **2 lines** (`cosmology:102`; `mesoamerica:58`), all by-product or disclaimer". Removes `:71` as a `cartograph` hit (it is a "survey maps"/"Mappa Mundi" hit, not the word). |
| 2 | "not carried" provenance | R02 §2.4 (`:131-136`), K01 (`scout/K01-gap-recheck.md:239`) | "the only pre-r47 proposal is the originating scout…" → "**no cartography proposal before r44 K02; the r44 K02 scout is the cited seed and was never drafted or landed**…" |
| 3 | `cosmology:27` disposition | R02 C-D2 (`:125`), X04 §3 | Append to the cosmology boundary row: "`:27`'s 'how the world is drawn (maps)' is the world model's drawn **content**; this entry owns the surveyed, projected, reproduced sheet as **production**." |
| 4 | craft ladder anchor | C08 P1-2 (`cov/C08-boundary.md:188-194`), R02 C-D4 (`:129`) | `craft-artisan-lexicon.md:44` for the ladder → `:56-63`; `:3` is the topic overview, `:44` stays cited only for material grading; marks stay `:76-87`. Landed entry has one occurrence (`C02 §7.3`). |
| 5 | four boundary rows | C08 P1-3/P1-4/P2-1 (`:195-205`), R02 C-D5 (`:131`) | Add `trade-economy-lexicon` (measures `:3,:49`; split-object `:92,:121`), `celestial-symbolism-calendars` (constellations `:70`, planet-as-god `:53`, calendar `:136`), `craft-artisan-lexicon` (ladder `:3,:56-63`, marks `:76-87`), `sacred-kingship-mythic-charter` (mythic charter `:3`) to C01 §1.1. |
| 6 | couples coverage | C08 P2-1; same authority as #5 | Add `../myth-symbol/sacred-kingship-mythic-charter.md` and `../myth-symbol/celestial-symbolism-calendars.md`; update `verified-at` from "21/21 couples paths" to "23/23". |

No other byte differs from the four filed fenced blocks. The `- topic:` line, the 8-field
order, the 20 `(to-verify)` marks, the NON-CANON example, the calibration bank and the scope
line are untouched.

### 3.5 Assembler (save as `.scratch/w02/assemble-landable.py`, run from the lane root)

It verifies all four fragment digests, applies §3.4, and refuses to write unless the result
matches the pin. `--check` is a dry run.

````python
#!/usr/bin/env python3
"""Assemble the r47 cartography entry from the four fenced fragments and apply
the C08/R02 corrections. Read-only over the repo; writes only to --out.

Exit 0 only when every fragment digest matches the pin and the assembled bytes
match the pinned digest. Any drift is a hard failure: re-pin and re-run the
audits, do not land silently.
"""
import argparse
import hashlib
import re
import sys

FRAGS = [
    ("C04", "reports/round-47/cov/C04-entry-header.md",
     "cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0"),
    ("C01", "reports/round-47/cov/C01-entry-a.md",
     "cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d"),
    ("C02", "reports/round-47/cov/C02-entry-b.md",
     "5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af"),
    ("C03", "reports/round-47/cov/C03-entry-c.md",
     "4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5"),
]
EXPECTED = "8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b"

ROWS_AFTER = {
    "| `myth-symbol/sacred-topography-pilgrimage.md` |":
        "| `myth-symbol/sacred-kingship-mythic-charter.md` | the mythic charter of rule and the royal register (`:3`) | the **legal charter** — the document that legitimates a claim to ground; the two charters' disagreement is a plot engine. This entry cites `:3` and does not restate the legitimation channels |",
    "| `myth-symbol/direction-symbolism.md` |":
        "| `myth-symbol/celestial-symbolism-calendars.md` | constellations and asterisms (`:70`), planet-as-god identities (`:53`), the sky-as-calendar machinery (`:136`) | the **star chart as a produced document** (observation, projection, print). The sky typology and calendar mechanics stay there |",
    "| `culture-material/writing-media-surface-economy.md` |":
        "| `culture-material/craft-artisan-lexicon.md` | the workshop register, seven guild/workshop systems, the apprentice\u2192journeyman\u2192master ladder (`:3`,`:56-63`), the six-type mark taxonomy (`:76-87`) | the **map trade's** roles, products, customers and licensing. This entry cites the ladder and the mark types and does not restate them (`:44` is the material-grading row, not the ladder) |",
    "| `culture-material/transport-mobility-lexicon.md` |":
        "| `culture-material/trade-economy-lexicon.md` | measures, weights and contract vocabulary (`:3`,`:49`,`:92`,`:121`) | the **map as a legal/territorial instrument** at the metrology boundary; a copied sheet authenticates by seal and counterpart, not by cutting. No metrology history is restated |",
}


def block(text):
    m = re.search(r"^(`{3,4})markdown\n(.*?)^\1[ \t]*$", text, re.M | re.S)
    if not m:
        raise SystemExit("no ```markdown fenced block")
    return m.group(2)


def replace_once(text, old, new):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"expected 1 occurrence, found {n}: {old[:70]!r}")
    return text.replace(old, new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=".scratch/w02/landable.md")
    ap.add_argument("--check", action="store_true",
                    help="write nothing; verify the assembled digest only")
    a = ap.parse_args()

    blocks = []
    for seat, path, want in FRAGS:
        raw = open(path, "rb").read()
        got = hashlib.sha256(raw).hexdigest()
        if got != want:
            raise SystemExit(f"{seat}: fragment digest drifted\n  want {want}\n  got  {got}")
        blocks.append(block(raw.decode("utf-8")).strip("\n"))

    text = "\n\n".join(blocks) + "\n"

    text = replace_once(
        text,
        "`grep -rli 'cartograph' \u2026` \u2192 **2 files / 3 lines**, all by-product or disclaimer "
        "(`cosmology-cosmography.md:71,:102`; `civilizations/mesoamerica-primary-sources.md:58`, "
        "lienzos as a source class);",
        "`grep -rli 'cartograph' \u2026` \u2192 **2 files** (`cosmology-cosmography.md`, "
        "`civilizations/mesoamerica-primary-sources.md`); `grep -rn 'cartograph' \u2026` \u2192 "
        "**2 lines** (`cosmology-cosmography.md:102`; "
        "`civilizations/mesoamerica-primary-sources.md:58`, lienzos as a source class), "
        "all by-product or disclaimer;",
    )
    text = replace_once(
        text,
        "**Not carried:** the only pre-r47 proposal is the originating scout "
        "`reports/round-44/scout/K02-gap-scout.md` (its \u00a73.6 checked every prior registry "
        "and found none), and",
        "**Not carried:** no cartography proposal before r44 K02; the r44 K02 scout "
        "`reports/round-44/scout/K02-gap-scout.md` is the cited seed and was never drafted "
        "or landed (its \u00a73.6 checked every prior registry and found none), and",
    )
    text = replace_once(
        text,
        "or the cosmogram typology |",
        "or the cosmogram typology. `:27`'s \"how the world is drawn (maps)\" is the world "
        "model's drawn **content**; this entry owns the surveyed, projected, reproduced "
        "sheet as **production** |",
    )
    text = replace_once(
        text,
        "craft-artisan-lexicon.md:44`; the guild ladder is at `:3`",
        "craft-artisan-lexicon.md:56-63`; the guild overview is `:3`",
    )
    text = replace_once(text, "21/21 couples paths resolve", "23/23 couples paths resolve")

    lines = text.split("\n")
    out = []
    for ln in lines:
        out.append(ln)
        for anchor, row in ROWS_AFTER.items():
            if ln.startswith(anchor):
                out.append(row)
    if len(out) != len(lines) + len(ROWS_AFTER):
        raise SystemExit("boundary-row anchors did not all match")

    idx = [i for i, l in enumerate(out) if l.startswith("- couples:")]
    if len(idx) != 1:
        raise SystemExit("expected exactly one - couples: line")
    i = idx[0]
    c = out[i]
    a1 = "this entry owns the map convention: orientation choice, compass rose, north arrow)"
    a2 = "cites the route types as map content)"
    if c.count(a1) != 1 or c.count(a2) != 1:
        raise SystemExit("couples insertion anchors not unique on the line")
    c = c.replace(
        a2,
        a2 + "; myth-symbol \u2014 `../myth-symbol/sacred-kingship-mythic-charter.md` "
        "(owns the mythic charter of rule and the royal register \u2014 `:3`; this entry "
        "owns the legal charter and cites the legitimation channels)",
    )
    c = c.replace(
        a1,
        a1 + "; myth-symbol \u2014 `../myth-symbol/celestial-symbolism-calendars.md` "
        "(owns constellations and asterisms \u2014 `:70`, planet-as-god identities \u2014 "
        "`:53`, and the sky-as-calendar machinery \u2014 `:136`; this entry owns the star "
        "chart as a produced document and does not restate the sky typology)",
    )
    out[i] = c
    text = "\n".join(out)

    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != EXPECTED:
        raise SystemExit(f"assembled digest drift\n  want {EXPECTED}\n  got  {digest}")
    print(f"lines {text.count(chr(10))} bytes {len(text.encode())} sha256 {digest}")
    if not a.check:
        open(a.out, "w", encoding="utf-8", newline="").write(text)
        print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

Measured run at spec time: `lines 797 bytes 130776 sha256 8fdb8bd7…`, exit 0.

**If a fragment is legitimately revised before apply:** the assembler fails closed. Do not
patch `EXPECTED` alone. Re-run C07/C08 and the source audit on the new bytes, re-derive the
pin, update `FRAGS` and `EXPECTED`, and record the new transcript. A pin change without a
re-audit is the r43 stale-premise defect in a new costume.

## 4. README rev 2.5 edit

### 4.1 Arithmetic

| vector | sum | status |
|---|---|---|
| rev-2.3 close (`corpus/README.md:20`) | `25/23/25/29/24/94` | 220 |
| rev-2.4 as first filed (`:11`) | `25/23/26/25/24/94` | **217** (6 short; the defect) |
| rev-2.4 repaired | `25/26/25/29/24/94` | 223 |
| rev-2.5 landing | `25/26/26/29/24/94` | **224** |

The repair is an in-place token fix at `corpus/README.md:11`; the defective reading is
preserved as a quoted dated record inside the new rev-2.5 block, following the file's own
convention (`corpus/README.md:550` in the live file).

### 4.2 Diff source and pin

The diff is **not** re-authored here. It is C09's fenced diff, extracted byte-for-byte:

- source: `reports/round-47/cov/C09-readme.md` (file sha256
  `b63df413410150b44705e8f9999d1bb73c3682daaeea66e0347dbff5152b3008`)
- extract: the `diff` fenced block in that file
- normalized diff sha256:
  `ebe78e8ef4d550758974451657d941d69342ac70edf32e9117e3e0811bb317b0` (14,560 bytes, 82 lines)
- `git apply --check` against the live tree: **exit 0** (measured)
- four hunks: rev-2.5 block + rev-2.4 vector repair; new row in filename order; totals
  223→224; footer vector + revision history

Extraction command (writes only to scratch):

```bash
python3 - <<'PY'
import hashlib, re
src = 'reports/round-47/cov/C09-readme.md'
t = open(src, encoding='utf-8').read()
d = re.search(r'^```diff\n(.*?)^```[ \t]*$', t, re.M | re.S).group(1)
assert hashlib.sha256(d.encode()).hexdigest() == \
    'ebe78e8ef4d550758974451657d941d69342ac70edf32e9117e3e0811bb317b0'
open('.scratch/w02/readme-rev25.diff', 'w', encoding='utf-8', newline='').write(d)
print(len(d), 'bytes')
PY
```

The new row is generated from the **landed** `- topic:` (`C09-readme.md:170-181`, which
reproduces `sweep.py:74-82`'s space-joining). Measured on the landable entry: 766 == 766
chars, row == topic **true**. If any edit changes the topic, regenerate the row and the diff;
do not hand-edit it.

### 4.3 Staged receipt (independently reproduced)

Method: copy `corpus/knowledge` (223 files) and `corpus/README.md` into
`.scratch/w02/e2e-final/`, write the landable entry at the target path, `patch -p1` C09's
actual diff, run the filed sweep through `sweep.sweep(readme_text, root_override=…)`.

| assertion | measured |
|---|---|
| patch apply | `patching file corpus/README.md`, rc **0** |
| rows == files | **224 == 224** |
| partition rows/files | civilizations 94/94, culture-material **26/26**, linguistics 25/25, myth-symbol 26/26, synthesis 29/29, verification 24/24 |
| missing / ghosts / topic mismatch / drift | `[] / [] / [] / {}` |
| totals line / footer | **224** / `224` with `[25, 26, 26, 29, 24, 94]` |
| footer findings | `[]`; `ok: true` |
| README sha256 after apply | `73985f68e48cbc7015eb00b1080796a5b93632eeb9b7ad76290074bf8de95afc` — **identical to C09's filed staged receipt** |
| corpus delta | exactly one added entry; no existing entry byte changed (`diff -qr` → only `cartography-and-mapmaking.md`) |

## 5. Exact apply sequence

Run from the lane root. Do not `git add`, commit or push. Steps 1–3 are mechanical; step 4
opens the corpus and must not start until the §8.1 length decision is recorded.

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/w02

# 0. Preflight — every line must hold.
test "$(git rev-parse HEAD)" = "6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe"
test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 223
test "$(ls corpus/knowledge/culture-material/*.md | wc -l)" -eq 25
test ! -e corpus/knowledge/culture-material/cartography-and-mapmaking.md
test "$(sha256sum corpus/README.md | cut -d' ' -f1)" = \
  7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
python3 -B reports/round-28/readme/sweep.py   # exit 0, rows 223 files 223

# 1. Assemble + verify the landable bytes.
#    Save the §3.5 script as .scratch/w02/assemble-landable.py first.
python3 .scratch/w02/assemble-landable.py --check
# expect: lines 797 bytes 130776 sha256 8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b

# 2. Extract + pre-check the README diff.
#    Run the §4.2 extraction snippet, then:
git apply --check .scratch/w02/readme-rev25.diff   # exit 0

# 3. (Gate §8.1 resolved.) Land the entry.
python3 .scratch/w02/assemble-landable.py --out .scratch/w02/landable.md
cp .scratch/w02/landable.md \
   corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 4. Apply the README edit only after the entry is in place.
git apply .scratch/w02/readme-rev25.diff

# 5. Verify (§6); then stop. Do not stage/commit.
```

Order is load-bearing: the README first would create a ghost row and footer drift; the entry
first gives the sweep a file to match.

## 6. Post-apply acceptance checks

Run all from the lane root. A failure in rows 1–5b is a landing failure, not a style note.

| # | check | command | expected |
|---|---|---|---|
| 1 | entry bytes | `sha256sum corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b` |
| 2 | totals | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l` | `224`; `26` |
| 3 | README bytes | `sha256sum corpus/README.md` | `73985f68e48cbc7015eb00b1080796a5b93632eeb9b7ad76290074bf8de95afc` |
| 4 | sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 224 files 224`, totals 224, footer `25/26/26/29/24/94`, exit 0 |
| 5 | entry contract — run **before** step 3 | extract C07's §7 checker to `.scratch/w02/check_c07.py` and run `python3 .scratch/w02/check_c07.py .scratch/w02/landable.md --root .` (target still absent) | **0 FAIL, 2 WARN** (README row absent; length 797) |
| 5b | C07 post-landing — expected flip | run the same checker on the landed path with `--root .` | exactly **2 FAIL**: `target path is free` and `no cartography topic owner`; both are expected because the target now exists. README row PASS; length WARN. Any other FAIL is a content failure. |
| 6 | README row == topic | §4.2 generator against the landed entry | `True`, 766 chars |
| 7 | rev vectors | `grep -n 'revision: 2.5\|revision: 2.4\|25/26/26/29/24/94\|25/26/25/29/24/94' corpus/README.md` | rev 2.5 at the top; rev 2.4 repaired to `25/26/25/29/24/94` = 223; rev 2.5 vector = 224 |
| 8 | boundary counts (C08 B1/B10–B13) | `for n in cosmology-cosmography sacred-topography-pilgrimage direction-symbolism architecture-settlement-lexicon writing-media-surface-economy mesoamerica-primary-sources transport-mobility-lexicon naming-systems craft-artisan-lexicon trade-economy-lexicon celestial-symbolism-calendars sacred-kingship-mythic-charter; do printf '%-40s %s\n' "$n" "$(grep -c "$n" corpus/knowledge/culture-material/cartography-and-mapmaking.md)"; done` | every name **≥1** |
| 9 | divination non-collision | `grep -nE '\bdivination\b|\bgeomanc|\bomen\b' corpus/knowledge/culture-material/cartography-and-mapmaking.md` | **0** lines (the two `omen` substrings are inside "phenomenon") |
| 10 | one-owner post-landing | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \| wc -l`; `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr)' corpus/knowledge/ \| wc -l` | `1` (the new file); `1` (its own topic) |
| 11 | worktree delta | `git status --porcelain`; `git diff --stat` | one new untracked corpus file + ` M corpus/README.md`; no other tracked change |
| 12 | couples resolution | C07 checker legs "repo/relative paths in couples resolve", "bare .md tokens unique/exist" | all pass; 23 tokens |

**Do not claim C08's B1–B16 all pass.** Rows B4 and B9 carry literal anchors the landable bytes
do not cite (`direction-symbolism.md:26`, `naming-systems.md:118`); C08's §4 did not classify
them P1. See §8.3.

## 7. Abort and rollback

| state | rollback | verify |
|---|---|---|
| nothing applied | — | preflight §2 still green |
| entry applied, README not | `rm corpus/knowledge/culture-material/cartography-and-mapmaking.md` | 223 files, 25 culture-material, sweep exit 0 |
| README applied, entry applied | `git apply -R .scratch/w02/readme-rev25.diff` then remove the entry | README sha `7c788a1d…`, 223 files, sweep 223==223 |
| `git apply` fails | do **not** force or hand-edit; stop and re-check the README sha | expected `7c788a1d…` |
| assembler digest drift | do **not** edit `EXPECTED`; stop and re-audit | §3.5 |

Do not use `git checkout -- corpus/README.md` blindly: it discards any concurrent edit. Read
`git diff corpus/README.md` first; the only intended hunk is C09's diff.

## 8. Open gates and residuals

### 8.1 Length (C-D1) — unresolved, blocking a clean `improved`

- landable: **797 lines**; live culture-material range 103–221, median 149, max 221; P02's
  stated bloat line 340; C07's checker band 100–260.
- C07's checker returns **WARN**, not FAIL (0 FAIL on the landable bytes). C11 §5 D1
  (`cov/C11-scribe.md:137`) calls it **BLOCKING** and says "do not land silently"; R02
  (`review/R02-review.md:113-123`) and X04 (`cross/X04-coverage-critic.md:194-200,231-241`)
  say coverage is `unchanged` on quality if the entry lands undeduplicated.
- Resolution: trim to ≤340 (or ≤260) and re-pin, **or** file an explicit C07/R03 waiver.
  R03's out path is absent at spec time, so the waiver must come from C07's author or the
  parent. Without one, record C as `unchanged`, not `improved`.

### 8.2 Stale pins in sibling fragments (do not copy)

| fragment | stale claim | measured / correct |
|---|---|---|
| `cov/C11-scribe.md:43-46` | 854 lines / 132,075 bytes / `bc12037c…` | raw 793 / 128,673 / `50c85471…`; landable 797 / 130,776 / `8fdb8bd7…` |
| `cov/C13-couples.md:10,53` | 21/21 couples | landable has **23/23** after the two C08 rows; re-run the resolver, do not assert `+21` or `2751` refs |
| `cov/C05-freshness.md:273,295` (per R02 `:96`) | vector `26/26/25/29/24/94` | correct `25/26/26/29/24/94` |
| `cov/C04-entry-header.md:59,115` | `cartograph` "2 files / 3 lines" | **2 files / 2 lines** (`cosmology:102`, `mesoamerica:58`); `:71` is not a `cartograph` hit |
| `cov/C04-entry-header.md:160` | "21/21 couples paths" | landable `verified-at` says **23/23**; the fragment's sentence is superseded |
| `cov/C02-entry-b.md:421,456` (seat-side, outside the fence) | certifies `craft-artisan-lexicon.md:44` as the ladder | `:44` is steel grading; ladder is `:56-63`. The landed entry is fixed; the C evidence chain still contains the false audit → record an erratum, do not edit filed bytes |

### 8.3 C08 checklist literals not met

- **B4** requires `direction-symbolism.md:26`; the entry cites `:51` and does not cite `:26`.
- **B9** requires `naming-systems.md:118` or `:136`; the entry cites `:70,:40,:97` and the
  celestial row's `:136` is a different file (`celestial-symbolism-calendars.md`).
- C08's §4 did not classify either as P1. The integrator should either add the anchors (a
  content decision, requiring re-pin) or record B4/B9 as named deviations; do not report a
  clean B1–B16 pass.

### 8.4 Length-related rebuild rule

If the integrator trims:
1. edit the assembled `.scratch/w02/landable.md` (or produce a trimmed assembly) — **never**
   edit filed fragments or the live corpus in place;
2. re-run the C07 checker and the staged sweep;
3. re-derive `sha256`; update `EXPECTED` and the §3.3 pin in this sheet's successor record;
4. re-run the C08 row counts and the couples resolver (trims can drop tokens);
5. record the new line count and the trim rationale.

## 9. Provenance

**Measured by this seat at HEAD `6e9a30d` on 2026-10-19:** HEAD/census/target absence; the four
fragment file and block digests; raw assembly 793/128,673/`50c85471…`; landable assembly
797/130,776/`8fdb8bd7…`; topic 766/`bc7274f4…` == seed; README row 801/`2ff30508…` == C09's
`+` line; couples 23 unique/23 resolve; C07 0 FAIL/2 WARN; staged `patch` rc 0; staged README
`73985f68…`; sweep 224==224, footer `25/26/26/29/24/94`; `git apply --check` 0; `git status`
shows no tracked corpus change. Every command and expected value is in §2, §3, §4.3, §6.

**Inherited, not re-authored:** C09's README diff and row generator; C08's P1 row text and
checklist; R02/X04's correction wording; K01's scoped provenance sentence; the 223-entry live
partition. C11's earlier staged receipt (854-line assembly) is superseded and is not used.

**Not done:** no corpus write, no staging under `corpus/`, no git add/commit/push, no network,
no filed-byte edit, no `run-validation.py`, no re-freeze, no packet change. This seat wrote
only this file plus disposable `.scratch/w02/` artifacts.

**to-verify:** the length waiver decision (owner: parent/C07); the B4/B9 anchors (owner:
content audit); C06/C12/C14 must re-run on the landable bytes before the C evidence chain is
cited — their earlier audits were pinned to superseded drafts.
