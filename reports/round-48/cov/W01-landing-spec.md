# W01 — C landing wire: exact apply instructions for the cartography entry + README rev 2.5

- Seat: `W01` | role: executor | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19),
  equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cov/W01-landing-spec.md` (this file; the only path this seat wrote)
- Mission (`reports/round-48/targets.json:53`): the integrator's exact apply — target path,
  byte source, README edit, sha pins
- Status: **APPLY SHEET, NOT AN APPLIED LANDING.** No `corpus/**` byte was written, staged, or
  edited. Every staging operation ran under `.scratch/w01/`.

## 0. Bottom line

Both byte sources are now filed and pinned, so this sheet is concrete: **entry** = C02's head
fence + C01's fence sliced at `## 1.` + **one** ledger correction (the agrarian boundary row that
C07 files as blocking U1) → **240 lines / 37,836 bytes / sha256 `d4cb0ee1…`**. **README** =
C10's Patch A (pre-Ca) or Patch B (post-Ca), both already `git apply`/`patch` verified, giving
**595 lines / `5767d3c4…`** or **593 lines / `3960c5e2…`**. Both staged 224 trees sweep green
with the landable entry (`rows 224 files 224`, footer `25/26/26/29/24/94`, exit 0).

Three things a naive apply would get wrong, all handled below:

1. **C01's fence is a whole entry, not a body.** It opens with its own H1 and a head block that
   lacks `- source:` and puts `- gap filled:` before `- topic:`. Lifting it whole alongside C02
   produces two H1s and a head that fails the contract. Slice at the first `## 1.` (§3.2).
2. **The boundary table omits `agrarian-field-system-lexicon.md`.** C07 files this as blocking
   under-claim (U1); E01 supplies the row. Without it the entry is not landing-ready (§3.5).
3. **Three README rev-2.5 prose variants exist** (C10 595 / D01 582 / this seat's fallback 587).
   All are sweep-green because no leg reads revision prose. Adopt C10's patch and do not
   "repair" a sha mismatch by editing bytes (§4.6).

Residual gates are honest: the arithmetic, citation, shelf and content auditors ran at read cuts
that predate these fragments. Their verdicts are **not** verdicts on `d4cb0ee1…` (§7).

## 1. Target and landing type

| item | value | evidence |
|---|---|---|
| target path | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `ls` → No such file or directory (measured) |
| landing type | **A** (add), never **M** | target absent; `git status --porcelain` → `?? reports/round-46/review/`, `?? reports/round-48/` only |
| sort slot | after `calendar-festival-systems.md`, before `costume-semiotics.md` | `ls corpus/knowledge/culture-material/ \| nl` → calendar 5, costume 6; `calendar` < `cartography` < `costume` |
| pre total / partition | **223** / culture-material **25** | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l` |
| post total / partition | **224** / culture-material **26** | staged sweep §4.4 |
| partition length band | min 103 / median 149 / mean 150.2 / max **221** (25 files) | `wc -l corpus/knowledge/culture-material/*.md` + Python median |
| landable length | **240** lines | assembler §3.4; ≤250 hard, >221 WARN |
| claim contract | `reports/round-48/claims.json:29-38` | ≤ ~250 lines; 224; 26; sweep green; prose vector 224; zero overwrites |

## 2. Preflight receipt (measured 2026-10-19 from the lane root)

`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` in every shell.

| # | check | command | measured | expected |
|---:|---|---|---|---|
| 1 | HEAD | `git rev-parse HEAD` | `a01405dd…cf6a0af` | baseline |
| 2 | total | `find corpus/knowledge -name '*.md' \| wc -l` | `223` | 223 |
| 3 | culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | `25` | 25 |
| 4 | target free | `test ! -e corpus/knowledge/culture-material/cartography-and-mapmaking.md` | true | absent |
| 5 | filename owners | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | `0` | 0 |
| 6 | topic owners | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr)' corpus/knowledge/ \| wc -l` | `0` | 0 |
| 7 | live sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, totals 223, footer `25/26/25/29/24/94`, exit 0 | green |
| 8 | sweep controls | `python3 -B reports/round-28/readme/sweep.py --selftest` | `selftest: 12/12 checks passed` | 12/12 |
| 9 | README sha | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | pin |
| 10 | README rev | `sed -n '5p'` | `revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three` | rev 2.4 |
| 11 | README H1s | `grep -c '^# ' corpus/README.md` | `2` (lines 1 and 3; Ca owns the duplicate) | unchanged by C |
| 12 | totals line | `sed -n '544p'` | `Total knowledge entries: 223.` | 223 |
| 13 | footer | `sed -n '548p'` | `(total 223 files; directory totals 25/26/25/29/24/94).` | 223 |
| 14 | rev-2.4 prose defect | `sed -n '11p'` | `25/23/25/29/24/94 → **25/23/26/25/24/94**` = **217** | repair |
| 15 | culture-material header | `sed -n '234p'` | `## culture-material/ (25)` | 25 |
| 16 | inventory | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `"files": 223` | 223 |

A moved HEAD is not automatically fatal, but rows 2–16 must be re-measured and the new HEAD
recorded; the claims baseline is `a01405d`.

## 3. Byte source (entry)

### 3.1 Fragment pins (measured now, not inherited)

| order | fragment | file sha256 | raw block sha256 | normalized block sha256 (pin) | block lines | slice |
|---:|---|---|---|---|---:|---|
| 1 | `reports/round-48/cov/C02-header.md` | `2ff5b15da54eba4ff2f99be0eac2ba6e584b3edf782ac546b6241b067bd96653` | `708dec15e0fb2563c258a680800e20892719c1480b0c364507c5799edf849816` | `4692a3347faf8efbdfcd8b3b362d6812ca7c7a1abc439ca644b6d13dc1feea38` | 23 | head, whole |
| 2 | `reports/round-48/cov/C01-entry.md` | `4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d` | `e52556572341bd82545f841cee01e7bf2c581c268910ff2a6f0c2f087cf44f84` | `85f07f1bb1f660558c12c66679a1b6a487ab2c940442db67cf302acb0d6c9ae3` | 227 | from first `## 1.` → 215 |

"Raw" is the fence body as captured, including the newline before the closing fence; "normalized"
is that body with leading/trailing newlines stripped — the bytes the assembler concatenates and
the only block digest the manifest should pin. The C01 **raw** block sha `e5255657…` is the digest
E02 audited as "the 227-line entry" (`cov/E02-register.md:7`), which confirms the block, not a
seat-side extract, is the audited object. C01's file sha moved during this seat
(`a075a9da…` → `4c2815a7…`) while the block stayed byte-identical: seat-side prose is not landing
bytes, so only block drift is fatal (§3.4).

### 3.2 Assembly rule, and why C01 is sliced

C02's block is the sanctioned head: 23 lines, eight fields in contract order
(`topic → gap filled → sources → couples → source → verified-at → recheck → scope`), 11 sha-pinned
in-corpus anchors. C01's block is a **complete entry** — H1 at its line 1, then
`- gap filled:` at line 3 and `- topic:` at line 4, and no `- source:` field. Lifting both whole
gives two H1s and a head that fails the eight-field gate. Therefore:

```
entry = C02_block + "\n\n" + (C01_block sliced at the first line starting "## 1.") + "\n"
```

No other bytes are added. The body's `## 1.` begins at C01 block line 13, so the slice is 215
lines and the assembly is 23 + 1 + 215 + 1 = **240** lines.

### 3.3 Manifest (exact, as run)

Save as `.scratch/w01/manifest.json`. The authoritative pin is **`block_sha256`**, the digest of
the fenced block *after* stripping the fence-adjacent newlines (the exact bytes the assembler
concatenates). `file_sha256` is advisory: a seat-side prose edit outside the fence moves it and
must not block assembly. Both values below were computed at spec time; if a **block** is revised,
re-pin **and re-run the audits** — never patch a digest alone. (Measured during this seat: C01's
file moved `a075a9da…` → `4c2815a7…` while its block stayed byte-identical, which is why the
block is the pin.)

```json
{
 "expected_lines_max": 250,
 "fragments": [
  {"seat": "C02", "path": "reports/round-48/cov/C02-header.md",
   "block_sha256": "4692a3347faf8efbdfcd8b3b362d6812ca7c7a1abc439ca644b6d13dc1feea38",
   "file_sha256": "2ff5b15da54eba4ff2f99be0eac2ba6e584b3edf782ac546b6241b067bd96653"},
  {"seat": "C01", "path": "reports/round-48/cov/C01-entry.md",
   "block_sha256": "85f07f1bb1f660558c12c66679a1b6a487ab2c940442db67cf302acb0d6c9ae3",
   "file_sha256": "4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d",
   "from": "## 1."}
 ],
 "corrections": [
  {"id": "L1",
   "authority": "reports/round-48/cov/E01-boundary.md:39 and :85; reports/round-48/cov/C07-boundary.md:197 (U1, blocking)",
   "find": "| `culture-material/transport-mobility-lexicon.md` | route institutions, maintenance (`:28,:117`) | representation of a route; cites the maintenance rule |",
   "replace": "| `culture-material/transport-mobility-lexicon.md` | route institutions, maintenance (`:28,:117`) | representation of a route; cites the maintenance rule |\n| `culture-material/agrarian-field-system-lexicon.md` | PARCEL and CLAIM institutions and their words — field names, boundary words, tenure words, land measures (`:42`, `:45`) | the drawn cadastral sheet; owns tenure *words*, not the sheet |"}
 ]
}
```

### 3.4 Assembler (tested fail-closed on both synthetic and real fragments)

Measured runs: as-filed (no correction) → `239 / 37,592 / d1de5db5…`; landable (L1) →
`240 / 37,836 / d4cb0ee1…`. The delivered code in this sheet, extracted verbatim and run against
the delivered manifest, reproduces `d4cb0ee1…` byte-identically. Block-digest drift, over-length,
nested fences, and missing/duplicated correction anchors each exit 1 with a named failure; a
file-digest drift (seat-side prose) warns and proceeds.

````python
#!/usr/bin/env python3
"""r48 C landing assembler (manifest-driven, fail-closed). Writes only --out."""
import argparse, hashlib, json, os, re, sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
HEAD_FIELDS = ["- topic:", "- gap filled:", "- sources:", "- couples:", "- source:",
               "- verified-at:", "- recheck:", "- scope:"]
BLOCK_RE = re.compile(r"^(`{3,4})markdown\n(.*?)^\1[ \t]*$", re.M | re.S)


def fail(msg):
    raise SystemExit("FAIL " + msg)


def topic_of_text(text):
    m = re.search(r"^- topic:(.*?)(?=\n- \w)", text, re.M | re.S)
    if not m:
        return None
    return " ".join(p for p in (ln.strip() for ln in m.group(1).strip("\n").splitlines()) if p)


def build(manifest):
    blocks = []
    for f in manifest["fragments"]:
        raw = open(os.path.join(LANE, f["path"]), "rb").read()
        if f.get("file_sha256"):
            got = hashlib.sha256(raw).hexdigest()
            if got != f["file_sha256"]:
                print(f'WARN {f["seat"]}: file digest drift (seat-side bytes, not landing '
                      f'bytes) want {f["file_sha256"]} got {got}')
        m = BLOCK_RE.search(raw.decode("utf-8"))
        if not m:
            fail(f'{f["seat"]}: no ```markdown fenced block')
        if "```" in m.group(2):
            fail(f'{f["seat"]}: nested fence inside block')
        block = m.group(2).strip("\n")
        got = hashlib.sha256(block.encode()).hexdigest()
        if got != f["block_sha256"]:
            fail(f'{f["seat"]}: block digest drift want {f["block_sha256"]} got {got}')
        if f.get("from"):
            ls = block.split("\n")
            hit = [i for i, ln in enumerate(ls) if ln.startswith(f["from"])]
            if len(hit) != 1:
                fail(f'{f["seat"]}: slice anchor {f["from"]!r} matched {len(hit)} lines')
            block = "\n".join(ls[hit[0]:]).strip("\n")
        blocks.append(block)
    text = "\n\n".join(blocks) + "\n"

    for c in manifest.get("corrections", []):
        n = text.count(c["find"])
        if n != 1:
            fail(f'correction {c["id"]} ({c["authority"]}): anchor count {n}, expected 1')
        text = text.replace(c["find"], c["replace"], 1)

    lines = text.split("\n")
    body = text.count("\n")
    if "\r" in text:
        fail("CRLF in assembled bytes")
    if re.search(r"^```", text, re.M):
        fail("fence marker leaked into assembled bytes")
    if body > manifest["expected_lines_max"]:
        fail(f"length {body} > {manifest['expected_lines_max']} (partition discipline)")
    h1 = [ln for ln in lines if ln.startswith("# ")]
    if len(h1) != 1 or not lines[0].startswith("# "):
        fail(f"H1 count {len(h1)}; single H1 must be line 1")
    head = text.split("\n## ", 1)[0]
    pos = -1
    for fld in HEAD_FIELDS:
        i = head.find("\n" + fld)
        if i < 0:
            fail(f"head field missing: {fld}")
        if i < pos:
            fail(f"head field out of order: {fld}")
        pos = i
    if "NON-CANON" not in text:
        fail("no NON-CANON marker")
    if "(to-verify)" not in text:
        fail("no (to-verify) marks")
    topic = topic_of_text(text)
    if not topic:
        fail("empty - topic:")
    couples = [ln for ln in text.splitlines() if ln.startswith("- couples:")]
    if len(couples) != 1:
        fail(f"{len(couples)} - couples: lines")
    toks = re.findall(r"`([^`]+\.md)`", couples[0])
    base = os.path.join(LANE, "corpus/knowledge/culture-material")
    unres = [t for t in toks if not (os.path.exists(os.path.join(base, t))
                                     or os.path.exists(os.path.join(LANE, "corpus/knowledge", t)))]
    if unres:
        fail(f"unresolved couples tokens: {unres}")
    return text, topic, body, len(toks), len(set(toks))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--out")
    a = ap.parse_args()
    text, topic, body, ntok, nuniq = build(json.load(open(a.manifest, encoding="utf-8")))
    print(f"lines {body} bytes {len(text.encode())} sha256 {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"topic_chars {len(topic)} topic_sha256 {hashlib.sha256(topic.encode()).hexdigest()}")
    print(f"couples_tokens {ntok} unique {nuniq}")
    if body > 221:
        print(f"WARN lines {body} > live partition max 221 (claim allows <=250)")
    if a.out:
        open(a.out, "w", encoding="utf-8", newline="").write(text)
        print("wrote", a.out)


if __name__ == "__main__":
    main()
````

Gates: digest integrity; no leaked fence; no CRLF; length ≤250 (hard) and >221 (WARN); exactly
one H1 on line 1; eight head fields present and ordered; `NON-CANON`; `(to-verify)`; non-empty
topic; one `- couples:` line; every backticked `.md` token resolves relative to
`corpus/knowledge/culture-material` or the corpus root.

### 3.5 Correction ledger

| id | severity | authority | what it does |
|---|---|---|---|
| **L1** | **blocking** | `cov/E01-boundary.md:39`, `:85`; `cov/C07-boundary.md:197` (U1) | adds the 13th boundary row for `agrarian-field-system-lexicon.md`, which owns PARCEL/CLAIM and tenure words (`:42`, `:45` — re-read live: the PARCEL and CLAIM table rows, verbatim) but not the drawn sheet |

Why L1 and not more:

- **B8/`:27` is already answered in C01's own table** (`myth-symbol/cosmology-cosmography.md` row
  cites `:27,:71,:102`; `:27` appears six times in the landable bytes). No correction needed.
- **C18's P4/P5 target report prose outside the fence.** `grep` on the assembled bytes for
  `claims.json:6`, `18/18`, and `Boone` → **0 hits** each; those strings live in C02's seat-side
  analysis, not in the head block. No landing correction.
- **C18 P2 (shelf/body mismatch)** is P2, not blocking, and the body names works the head's
  18-item shelf omits. Recorded as a named deviation; do not silently expand the shelf.
- Nothing else in the filed fragments is classed blocking *against these bytes*. If C03/C04/C12
  finish on `d4cb0ee1…` and file findings, they become L2… with exact `find`/`replace`; the
  assembler refuses a correction whose anchor is not unique.

### 3.6 Assembled measurements (the pins)

| measurement | as-filed (no L1) | landable (with L1) |
|---|---|---|
| lines / bytes | 239 / 37,592 | **240 / 37,836** |
| sha256 | `d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1` | **`d4cb0ee17f0662a6c15cacfbd9e5c633fc0452570d94d7c322cef5c859caf508`** |
| H1 / H2 | 1 / 14 | 1 / 14 |
| head fields | 8, ordered | 8, ordered |
| `- topic:` | 766 chars, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495` | identical — byte-equal to the r44 seed (`reports/round-44/scout/K02-gap-scout.md:227`) |
| `- couples:` | 19 tokens, 19 unique, 19/19 resolve | identical |
| partition max | 221 | 240 (WARN: 19 over max; 10 under the hard 250) |

## 4. README rev 2.5 edit

### 4.1 Arithmetic (recomputed, not copied)

| vector | sum | status |
|---|---:|---|
| rev-2.3 close (`corpus/README.md:20`) | `25/23/25/29/24/94` = 220 | historical |
| rev-2.4 as filed (`:11`) | `25/23/26/25/24/94` = **217** | **live defect** (6 short of 223) |
| rev-2.4 repaired (`:11`) | `25/26/25/29/24/94` = **223** | this edit |
| rev-2.5 landing (`:5`) | `25/26/26/29/24/94` = **224** | this edit |

Note: `reports/round-48/targets.json:28` words the repair as "(synthesis 25→29, myth-symbol
23→26, culture-material 26→25 = 224)". The token changes are right but **"= 224" is wrong** —
that repaired vector sums 223. Do not copy that clause; the landing vector is the separate
`25/26/26/29/24/94` = 224.

### 4.2 Byte source: C10's patches (primary), not a fourth draft

C10 is this round's C-claim README executor and has already produced order-specific diffs,
extracted and re-verified here:

| patch | base | patch sha256 | base lines | post lines | post README sha256 | apply check |
|---|---|---|---:|---:|---|---|
| **A** | live README 575 lines / `7c788a1d…` | `80625041661bfd2dab9582e257c6f24f1e0c8ca03f2cb3d90a12d37750c211ba` | 575 | **595** | `5767d3c43d286e0863c44c55cfd1ebe8d13e7d8cd5a19c5d2c3424bc0e25648f` | `git apply --check` exit **0** |
| **B** | post-Ca README 573 lines (H1 at `:3` + its blank removed) | `12dd7dcddec377c3c3425120d552d3ce3978e2048e90529b22f1f2e0ed41b556` | 573 | **593** | `3960c5e2753a1cb2f8a7345b9f7210ad35405da9fe1189f0fb590772a22cebc7` | `patch -p1 --dry-run` exit **0** |

Extraction (writes only to scratch):

```bash
python3 - <<'PY'
import re, hashlib
t = open('reports/round-48/cov/C10-readme.md', encoding='utf-8').read()
d = re.findall(r"(?ms)^```diff\n(.*?)^```[ \t]*$", t)
want = ['80625041661bfd2dab9582e257c6f24f1e0c8ca03f2cb3d90a12d37750c211ba',
        '12dd7dcddec377c3c3425120d552d3ce3978e2048e90529b22f1f2e0ed41b556']
for i, (block, w) in enumerate(zip(d, want), 1):
    assert hashlib.sha256(block.encode()).hexdigest() == w, i
    open(f'.scratch/w01/c10-patch-{i}.diff', 'w', encoding='utf-8', newline='').write(block)
print('ok', [len(x) for x in d])
PY
```

C10's Patch A hunk 1 carries the two H1s as context, so it fails on a post-Ca tree (hunk 1 only);
that is why Patch B exists. Use **A when Ca has not landed**, **B when it has**. The two patches
are the same content edit (net +20 lines; +24/−4 across 3 hunks) anchored differently.

### 4.3 Fallback editor (only if a patch anchor drifts)

This seat also built a content-anchored editor; its six anchors are the live strings, each
occurrence count 1. It is **not** the primary wire because it would create a third rev-prose
variant. Measured variants: no-Ca `587` / `06807fc7…`; Ca removes `:3–:4` → `585` / `8b7d0e5a…`;
Ca removes `:3` only → `586` / `bb57eb2b…`. If used, record which variant landed and re-derive
the sha; do not compare it against C10's pin.

### 4.4 The row is generated, never hand-typed

The sweep compares the row text to the entry's `- topic:` after continuation lines are
space-joined (`reports/round-28/readme/sweep.py:66-82`; `ROW_RE` at `:60`). For this landing the
topic is **766 chars / `bc7274f4…`**, byte-equal to the r44 seed (independently confirmed at
three points by `cov/C16-topic.md:8`). The row is therefore **801 chars /
`2ff3050862ed6b8487e8bbb69e6e214eaa6936731570ad74e01a429ffd6d9e2c`**, identical to C10's `+`
line. If C01/C02 revise the topic, regenerate with `sweep.topic_of()` and re-run the patches; do
not reuse this pin.

### 4.5 C/Ca ordering (measured)

| order | what applies | result |
|---|---|---|
| **C first, then Ca** | Patch A on live README (595 lines, `5767d3c4…`), then Ca01 removes the duplicate H1 | final README is Ca01's; C's delta is Patch A |
| **Ca first, then C** | Ca01 produces the 573-line single-H1 file, then Patch B (593 lines, `3960c5e2…`) | final README `3960c5e2…` |

Both staged trees sweep green with the landable entry (`rows 224 files 224`, 0 topic mismatch,
footer `[25,26,26,29,24,94]`). A frozen diff built on the live README fails on a post-Ca base
(`patch -p1 --dry-run` → exit 1, "Reversed (or previously applied) patch detected", 3 hunks
ignored) — that is the trap Patch B exists to avoid.

### 4.6 Divergence record: three rev-2.5 prose variants

| source | staged README | sha256 | note |
|---|---|---|---|
| `cov/C10-readme.md` Patch A | 595 lines | `5767d3c4…` | **adopt** (claim executor) |
| `cross/D01-delta-receipt.md` | 582 lines, H1 count 1 | `4db8ecaf…` | stages Ca's H1 removal in the same edit; an 8-line rev block |
| this sheet's fallback editor | 587 lines | `06807fc7…` | not for delivery |

All three are sweep-green because no sweep leg reads revision prose (C10 §2.3 demonstrates the
control: reverting the 217-sum defect leaves the sweep green). The delivery certificate is the
**post-apply sweep receipt**, not a README sha; D01's own structural-digest rule says the same
(`cross/D01-delta-receipt.md:2`, `:141-162`). Do not reconcile a sha mismatch by editing bytes.

## 5. Exact apply sequence

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/w01

# 0. Preflight — §2 rows 1–16. Any miss: stop.
test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 223
test "$(ls corpus/knowledge/culture-material/*.md | wc -l)" -eq 25
test ! -e corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 1. Assemble (dry run), then land the entry (A).
#    Save §3.3 as .scratch/w01/manifest.json and §3.4 as .scratch/w01/assemble.py first.
python3 .scratch/w01/assemble.py .scratch/w01/manifest.json
#    expect: lines 240 ... sha256 d4cb0ee17f0662a6c15cacfbd9e5c633fc0452570d94d7c322cef5c859caf508
python3 .scratch/w01/assemble.py .scratch/w01/manifest.json --out .scratch/w01/landable.md
cp .scratch/w01/landable.md corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 2. Extract and apply the README patch (§4.2) — A if Ca has not landed, B if it has.
git apply --check .scratch/w01/c10-patch-1.diff     # or: patch -p1 --dry-run < ...-2.diff
git apply .scratch/w01/c10-patch-1.diff             # or: patch -p1 < ...-2.diff

# 3. Verify (§6). Stop. Do not git add, commit, or push.
```

Order is load-bearing: entry first, README second. README first creates a ghost row and footer
drift; entry first gives the sweep a file to match.

## 6. Post-apply acceptance checks

| # | check | command | expected |
|---:|---|---|---|
| 1 | entry bytes | `sha256sum corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `d4cb0ee17f0662a6c15cacfbd9e5c633fc0452570d94d7c322cef5c859caf508` |
| 2 | census | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l` | `224`; `26` |
| 3 | sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 224 files 224`, totals 224, footer `25/26/26/29/24/94`, `missing 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, exit 0 |
| 4 | row == topic | regenerate the row with `sweep.topic_of()` | empty diff |
| 5 | headings | `grep -c '^# ' corpus/README.md`; `grep -c '^## ' corpus/README.md` | `2` and `7` if Ca pending; `1` and `7` if Ca landed |
| 6 | rev vectors | `grep -n 'revision: 2.5\|25/26/25/29/24/94\|25/26/26/29/24/94' corpus/README.md` | rev 2.5 first; rev 2.4 repaired to 223; rev 2.5 vector 224 |
| 7 | entry length | `wc -l corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `240`; record any change |
| 8 | one owner | filename + topic probes | `1` (new file); `1` (its own topic) |
| 9 | no overwrite | `git status --porcelain`; `git diff --stat` | `??` new entry + ` M corpus/README.md`; no other corpus path |
| 10 | agrarian row | `grep -c 'agrarian-field-system-lexicon' corpus/.../cartography-and-mapmaking.md` | `≥1` (L1 present) |
| 11 | couples resolve | assembler re-run on the landed file | 19/19 |

## 7. r47 defect-class guard — evidence status, not a clean bill

R03's nine blocking defects (`reports/round-47/review/R03-c-content.md` §5.1) are the regression
set. This is what is actually verified on `d4cb0ee1…`:

| defect | gate | status on the landable bytes | authority |
|---|---|---|---|
| **B1** arithmetic (200 m = 20×) | G-ARITH | **could-not-evaluate** — C03 audited the r47 790-line fixture (7 FAIL), not these bytes | `cov/C03-arithmetic.md:183-251` |
| **B2** gap count | G-GAP | **pass by construction**: C02's `- gap filled:` says `cartograph` = 2 files / **2** lines; re-run `grep -rni 'cartograph' corpus/knowledge/` at apply and compare | `cov/C02-header.md`; measured 2 lines (`cosmology:102`, `mesoamerica:58`) |
| **B3** false quote accusation | G-QUOTE | **pass**: `coup` appears 4× incl. the verbatim `:70` quote; `archive of renamings` → 0 hits | `grep` on landable |
| **B4** ladder anchor | G-ANCHOR | **pass in the head/body**: `54-65` appears 3×; `:44`-as-ladder → 0 | `grep`; C02 head |
| **B5/B6** cross-refs | G-XREF | **could-not-evaluate** — no section-number audit on these bytes | C04 draft verdict `could-not-evaluate` (`cov/C04-citations.md:6`) |
| **B7** worked example | G-EXAMPLE | **could-not-evaluate** on these bytes (C14's live verdict is on M01); assembler confirms one NON-CANON marker and one example section | `cov/C14-example.md` |
| **B8** `:27` competing sentence | G-BOUND | **pass**: boundary row cites `:27,:71,:102`; `:27` appears on 6 lines | `grep -c` on landable |
| **B9** 5-of-8 forms | G-FORM | **could-not-evaluate** — count forms vs minimum-build rows at apply | C03 `ARITH-6` |
| **U1** agrarian omission | G-BOUND | **fixed by L1** | `cov/C07-boundary.md:197`; `cov/E01-boundary.md:39` |
| **P2-3** volume | G-LEN | **pass**: 240 ≤ 250; WARN vs live max 221 | `wc -l` |

**Apply rule:** G-ARITH, G-XREF, G-EXAMPLE and G-FORM are open. The integrator may land only
with either (a) a filed verdict on `d4cb0ee1…` for each, or (b) an explicit record that they are
`could-not-evaluate` and the claim's "audits PASS" threshold is **not** met. Do not present the
r47 audits, or audits on `e5255657…`/`d1de5db5…`, as clearing these bytes.

## 8. Abort and rollback

| state | rollback | verify |
|---|---|---|
| nothing applied | — | §2 green |
| entry applied, README not | `rm corpus/knowledge/culture-material/cartography-and-mapmaking.md` | 223 / 25; sweep exit 0 |
| entry + README applied | `git apply -R` the same patch (or `patch -R`), then remove the entry | README sha back to `7c788a1d…` (or Ca's pre-state); 223 / 25; sweep exit 0 |
| assembler fails | do **not** edit the manifest digest to match the file | read the failure; re-pin only after re-running the audits |
| correction anchor count ≠ 1 | do not force | re-measure the assembled bytes; re-derive the anchor from E01's live row |

Never use `git checkout -- corpus/README.md` blindly: it discards a concurrent Ca edit.

## 9. Open items (`to-verify`, with owners)

| item | owner | why it is open |
|---|---|---|
| G-ARITH / G-XREF / G-EXAMPLE / G-FORM verdicts on `d4cb0ee1…` | C03, C04, C14, C12/R03 | their filed audits ran before these fragments existed |
| C18 P2 shelf/body mismatch (P2) | C08/C18 or integrator | body names works absent from the 18-item shelf; recorded as a named deviation, not corrected |
| final joint README sha (C + Ca) | integrator | depends on which of §4.5's orders is used and on Ca01's exact whitespace choice; the sweep receipt is the certificate |
| C05 length-contract and C12 content fragments | their seats | not filed at spec time; the assembler's G-LEN is the only length check yet run on these bytes |

## 10. Provenance and write surface

**Measured by this seat at HEAD `a01405d`, 2026-10-19:** §2 rows 1–16; partition band (25 files,
min 103, median 149, mean 150.2, max 221); vector sums 220/217/223/224; fragment file digests and
both raw and normalized block digests (`C02 4692a334…`, `C01 85f07f1b…`); the live C01 file-drift
observation (`a075a9da…` → `4c2815a7…` with the block unchanged); as-filed assembly
`239 / 37,592 / d1de5db5…`; landable assembly `240 / 37,836 / d4cb0ee1…`; the delivered
assembler + manifest re-extracted and re-run to the same `d4cb0ee1…`; topic 766 / `bc7274f4…`;
19/19 couples; C10 patch shas and both post-apply shas; Patch A `git apply --check` exit 0 and
hunk 1 failing on a post-Ca base; Patch B `patch --dry-run` exit 0 on a 573-line post-Ca file;
staged 224 sweeps green for both orders with the landable entry;
`agrarian-field-system-lexicon.md:42` and `:45` re-read live.

**Not done:** no `corpus/**` write or staging, no git add/commit/push, no network, no install, no
filed-byte edit, no `run-validation.py`, no re-freeze, no packet change. This seat wrote only
this file plus disposable `.scratch/w01/` artifacts.

**Inherited, not re-authored:** C02's head and C01's body (their bytes); E01's agrarian row and
C07's U1 ruling; C10's README patches; C18's head-provenance findings; C16's topic confirmation;
the target path and topic seed from `reports/round-44/scout/K02-gap-scout.md`.
