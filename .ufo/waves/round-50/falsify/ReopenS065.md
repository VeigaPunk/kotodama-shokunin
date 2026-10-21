# ReopenS065 — attack on SOURCES row S065 (AHD 5th ed., Appendix I, s.v. *peku-)

Seat: `KotodamaR50-2.ReopenS065-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below were read with `git show <sha>:<path>`; the working tree was not trusted for any landed claim.
No lane file, index, jj state or fleet path was touched; no clones, installs or background jobs.

## Verdict

**HOLDS.** The URL opens natively (HTTP 200, no bot wall, no redirect, no archive fallback), the Gate quote is
byte-identical at the stated location, the tier/scope are honest under `corpus/QUALITY.md` criterion 6, and the
only knowledge-entry sentence that cites S065 is supported verbatim by the page. Three precision notes are recorded
at the end; none changes the verdict and no fix is required for the landed work.

## Evidence

### 1. URL opened this session (2026-10-21)

```
$ curl -sS -L --max-time 60 -o /tmp/ahd.html -w 'HTTP=%{http_code} final=%{url_effective} size=%{size_download} type=%{content_type}\n' \
    'https://www.ahdictionary.com/word/indoeurop.html'
HTTP=200 final=https://www.ahdictionary.com/word/indoeurop.html size=1763337 type=text/html; charset=UTF-8
```

The fragment `#IR084700` is not sent to the server; the base page was fetched and the anchor resolved inside it.
The page identifies itself as the AHD roots appendix, and its own metadata/footer place it in the Fifth Edition:

```
<title>Appendix I - Indo-European Roots</title>
<h2>The American Heritage Dictionary Indo-European Roots Appendix</h2>
<meta name="description" content="The much-anticipated Fifth Edition of The American Heritage Dictionary of the English Language is the premier resource ...">
Copyright  2022 HarperCollins Publishers All rights reserved.
```

Anchor presence and uniqueness:

```
$ grep -n -o 'name="IR084700"[^>]*' ahd.html
1394:name="IR084700"

$ python3 - <<'EOF'   # counts over the full page
print('quote occurrences:', h.count('Wealth, movable property. Oldest form'))
print('IR084700 occurrences:', h.count('IR084700'))
print('name="peku-" occurrences:', h.count('name="peku-"'))
EOF
quote occurrences: 1
IR084700 occurrences: 1
name="peku-" occurrences: 1
```

Both anchors sit on the same table cell as the `peku-` headword, so `#IR084700` lands on the cited entry.

### 2. Gate quote is byte-identical

Gate bullet, `corpus/lessons/round-50.md:50` (inside `## Gate`, heading at `:27`, next heading `## Status and used-by change log` at `:56`):

> S065 — https://www.ahdictionary.com/word/indoeurop.html#IR084700 — accessed 2026-10-21 — entry *peku-, headword gloss: "Wealth, movable property. Oldest form *pek̑u‑, becoming *peku‑ in centum languages." Seat: SrcPeku.

Character-level comparison of the quoted string against the live page (tags stripped only inside `<i>`):

```
page quote : 'Wealth, movable property. Oldest form *pek̑u‑, becoming *peku‑ in centum languages.'
gate quote : 'Wealth, movable property. Oldest form *pek̑u‑, becoming *peku‑ in centum languages.'
EQUAL: True
lens 83 83
codepoints page: ['0x311', '0x2011']
codepoints gate: ['0x311', '0x2011']
```

The combining inverted breve (U+0311, the palatovelar mark in `*pek̑u‑`) and the non-breaking hyphen (U+2011)
are reproduced exactly on both sides. This is not a normalized or retyped match.

### 3. Stated location is exact

Raw page region around the anchor (line 1394 in the fetched HTML):

```
<a name="IR084700"></a><a name="peku-"></a><b><font ...>peku-</font></b><br/>
Wealth, movable property. Oldest form <i>*pek̑u‑</i>, becoming <i>*peku‑</i> in centum languages.<ol>...
```

The quoted sentence is the line immediately under the headword and before the numbered reflexes — exactly the
"headword gloss" the row and Gate name. `corpus/SOURCES.md:94` locates it as "entry *peku-, headword gloss", and
that is accurate.

### 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6):

> **Source authority stays claim-scoped** — publisher descriptions and abstracts are tier B for substantive claims
> about a work, even when accurate; reserve tier A for sources primary or authoritative for the exact scope.

Row fields (`corpus/SOURCES.md:94`):

| field | value |
|---|---|
| source | The American Heritage Dictionary of the English Language, 5th ed., Appendix I Indo-European Roots, s.v. *peku- |
| kind | book |
| tier | B |
| scope | the dictionary gloss of PIE *peku- and its Latin reflexes; lexical derivation only, never PIE social history |

The page delivers exactly that scope and nothing more: it prints the root gloss, its oldest reconstructed form and
centum-language development, then English/Latin reflexes. It contains **zero** occurrences of the string
"livestock" (`grep -o -i 'livestock' ahd.html | wc -l` → `0`) and no statement about herding, PIE society,
archaeology or dating. Tier B ("strong secondary … textbook", `corpus/SOURCES.md:15-18`) is therefore honest and,
if anything, conservative: the dictionary is authoritative for its own gloss but only a synthesis for PIE
semantics, which is the scope the row states. No criterion-6 violation.

### 5. Every knowledge-entry sentence citing S065 is supported

`grep -n 'S065'` on the landed entry returns two lines:

- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:7` — shelf listing label only:
  `S065 AHD *peku-*`. Supported: the cited page is the AHD roots appendix, entry `peku-`.
- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:79` — the one substantive citation:

```
| Livestock → wealth | PIE *peku- glossed "wealth, movable property" (S065); Latin *pecūnia* (`trade-economy-lexicon.md:69`) | model as a documented change path; never print the root as settled social history |
```

The quoted gloss `"wealth, movable property"` is verbatim on the page (evidence §2). The cell's other half is
attributed in-corpus, not to S065; checked anyway at `corpus/knowledge/culture-material/trade-economy-lexicon.md:69`,
which reads `fee, pecuniary | Gmc *fehu*, Lat. pecūnia < pecus 'cattle' | PIE *peḳu- 'movable wealth = cattle' (Watkins)`,
consistent with the entry. The row's own support list — "Latin pecūnia and pecūlium" — is also on the page:

```
<li type="1">Suffixed form <i>*peku-n‑</i>.  pecuniary; impecunious, from Latin <i>pecūnia</i>, property, wealth.</li>
<li type="1">Suffixed form <i>*peku-l‑</i>.  peculate, peculiar, from Latin <i>pecūlium</i>, riches in cattle, private property.</li>
```

So the sentence the entry actually grounds in S065 is fully supported, and the design rule ("never print the root as
settled social history") is the correct hedge for what the dictionary actually says.

### 6. Registry shape and integrity

- Row at `corpus/SOURCES.md:94`; `awk -F'|' 'NR==94{print NF-2}'` → **11 columns**, matching the header at `corpus/SOURCES.md:25`.
- ID unique: `grep -o '^| S0[0-9][0-9]' | sort | uniq -d` → no output; 69 registry rows total.
- `status: mined` is consistent with the registry rule (`corpus/SOURCES.md:19-20`): the row's `used-by` names
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, and that file cites S065 at `:7` and `:79`.
- Access date `2026-10-21` matches both the Gate bullet and this session's live fetch.
- `Seat: SrcPeku` appears on both the S065 and S066 bullets (`corpus/lessons/round-50.md:50-51`). This is not a
  copy-paste error: the seat's own landed report `.ufo/waves/round-50/build/SrcPeku.md` records that it opened the
  D-PLACE EA004 variable as "the calibration companion to the hunting entry's EA001 row (S042)" in the same seat.
- The Gate preamble (`corpus/lessons/round-50.md:29-31`) requires every S048–S069 row to have been opened by the
  build seat named in its bullet, with a report under `.ufo/waves/round-50/build/`. `build/SrcPeku.md` exists and
  documents the AHD open, its native 200 route and the anchor, matching this session's independent fetch.

### 7. Independent corroboration of the access route

`build/SrcPeku.md` states: "`https://www.ahdictionary.com/word/indoeurop.html` rendered natively (200; the parsed
appendix ran to 8,196 lines); the entry is at `<a name="peku-">` / anchor `IR084700` … No bot wall, no archive
fallback." My fetch matches: 200, native HTML, anchor present once, no redirect. The scout also correctly warns not
to write "Watkins" into the row without checking the print edition; the landed row does not attribute Watkins, so
that caution was honored.

## Precision notes (non-blocking, no fix required)

1. **Headword typography.** The page prints the headword bold as `peku-` with no literal leading asterisk; the
   asterisk in the row/Gate (`entry *peku-`) is the standard reconstruction convention and appears as such in the
   entry's own prose (`*pek̑u‑`, `*peku‑`). Not a mismatch in substance.
2. **"livestock" in the row's teach column.** `corpus/SOURCES.md:94` says "livestock/movable-wealth gloss". The
   *headword gloss* says only "Wealth, movable property"; the livestock/cattle sense appears in the same entry's
   descendant glosses (`fē`, `feoh` "cattle"; `pecus` "cattle"; `pecūlium` "riches in cattle"). The entry's citing
   sentence (§5) quotes only the headword gloss, so no unsupported claim reaches the knowledge file. If the lane
   ever wants the column to mirror the headword line exactly, the append-only registry rule
   (`corpus/SOURCES.md:10-13`) would require a superseding row, not an in-place edit — not warranted on this
   evidence.
3. **Edition label.** The appendix body prints no edition string; "5th ed." is supported by the site's own metadata
   ("…Fifth Edition of The American Heritage Dictionary…") and the `Copyright 2022 HarperCollins` footer, and the
   page title gives "Appendix I - Indo-European Roots". The row does not attribute the appendix to Watkins, which is
   the right call given the page carries no byline.

## Out-of-scope observation (not part of this verdict)

`reports/round-50/validation.json`, named in the dispatch context as the round receipt, is **not present** in the
landed commit: `git cat-file -e 1c779e4a…:reports/round-50/validation.json` →
`fatal: path 'reports/round-50/validation.json' exists on disk, but not in '1c779e4a…'`. It exists only in the
working tree. This does not affect any S065 fact above, which was verified from the live page and landed bytes
alone; flagging it only because landed-claim discipline reads the commit, not the tree.

## Commands run (all read-only)

```
git -C … show 1c779e4a…:corpus/SOURCES.md | grep -n -A3 -B3 'S065'
git -C … show 1c779e4a…:corpus/lessons/round-50.md | grep -n -B4 -A8 'S065'
git -C … show 1c779e4a…:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -n 'S065'
curl -sS -L … https://www.ahdictionary.com/word/indoeurop.html
grep -n -o 'name="IR084700"[^>]*' /tmp/ahd.html
python3  # byte comparison, anchor/quote counts, codepoints
git -C … grep -n 'SrcPeku' 1c779e4a… -- .
```

Temporary artifact `/tmp/ahd.html` (1.7 MB) was deleted after the checks; no clone was created and nothing was
installed.
