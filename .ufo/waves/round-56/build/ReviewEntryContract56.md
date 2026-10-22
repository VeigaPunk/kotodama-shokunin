# ReviewEntryContract56 — claim C entry contract attack (round 56)

- Seat: KotodamaR56.ReviewEntryContract56 (leaf; no delegation, no background jobs).
- Date: 2026-10-22. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. Read-only: the only file this seat wrote is this report. No git or jj write anywhere.
- Read: reports/round-56/claims.json; .ufo/waves/round-50/build/ReviewEntryContract.md §2 (the r48/r49 eight-field head plus body shape, still the template); corpus/QUALITY.md criteria 1-5 (6-11 read for context); corpus/lessons/round-55.md `## Falsify` (line 195) and `## Mistakes`; corpus/lessons/round-55-verifier-spotcheck.md; corpus/SOURCES.md header and rows; tools/check-gate-quotes.py docstring; reports/round-56/accept-c.py; the round-55 entry corpus/knowledge/myth-symbol/monsters-hybrid-beings.md as the demonstration body.
- Axes judged: coverage (the checklist covers every routed failure mode), calibration (each check shown to run clean on real landed bytes and to fire on a mutated copy).

## 0. Result

No blocker. The declared instruments already cover six of the nine failure modes mechanically (accept-c legs SET/SWEEP/FLOOR/RANGE/STATUS/USEDBY/ACCESS; O's `tools/check-gate-quotes.py` after it lands). Three failure modes have no declared leg at all — wrong locators, dropped hedges, and over-reads of a row's kind/tier — and two more (draft ids, HTML entities in the entry bytes) are only covered indirectly. This report gives each failure mode one mechanical check, demonstrated on the round-55 entry `monsters-hybrid-beings.md` (73 cited ids, 188 lines), with a mutation control showing the check fires.

Real findings already visible in landed round-55 bytes (they calibrate the boundaries, they are not round-56 work): the round-55 lesson carries two draft ids as errata mentions (`corpus/lessons/round-55.md:149,151`); `corpus/SOURCES.md` carries HTML character references in three pre-S359 rows (`:275` S246, `:349` S320, `:361` S332); the pre-O checker prints 0 findings on round-55.md, proving the html-entity class is not landed yet.

## 1. Coverage map: what already checks what

| failure mode | declared instrument | gap |
|---|---|---|
| S-ids outside S359-S418; range notation; one row per id | accept-c.py RANGE leg (`reports/round-56/accept-c.py:33-35,97-100`) | none |
| cited row mined; used-by names the entry as a whole item | STATUS, USEDBY legs | none |
| at least 20 distinct S-ids | FLOOR leg | none |
| file set 231 -> 232, README index, counts | SET, SWEEP legs | none |
| ordinary-means access markers | ACCESS leg (`tools/check-source-access.py`) | none |
| Gate Grounds vs registry teaches; Gate entities; quote cap | O lands the html-entity class in check-gate-quotes.py (claims O, ENTITY/NOFALSE/DECODE legs) | only after O lands; see FM8 sequencing |
| wrong locators | none | FM1 below, review-pointer only |
| one case generalised to all Bantu/Africa | none (review-only clause) | FM2 below, probe |
| dropped hedges | none (review-only clause) | FM3 below, one-directional |
| catalogue record over-read as a study | none | FM4 below, probe |
| publisher blurb used as tier A | none (QUALITY criterion 6 is prose) | FM5 below, row-level |
| draft ids left in text | none | FM6 below |
| HTML entities in entry or new registry rows | O covers the lesson's Gate only | FM9 below |
| entry-local `[S##]` keys colliding with registry ids | none (round-55 Frontier item) | FM10 below |

The round-50 contract's shape commands stay required for the new entry (adapted paths): sweep, check-readme-heading.py, check-readme-revisions.py, provenance-audit.py, basename-couples-resolver.py (`ReviewEntryContract.md:§2.8`), length cap 230 lines for round 56 (claim C, at most 230 lines).

## 2. The checklist: failure mode, check, demonstration

All demonstrations ran in memory against the lane's landed bytes on 2026-10-22; no lane file was touched. "Landed" is the check on the real entry; "mutated" is the same check after a one-string change in memory, proving it fires.

### FM1 — wrong locators

Failure: the entry cites `(Sxxx, locator)` with a locator the opened page does not carry at that place. Round 55 fixed exactly this class: S353 `¶2` -> `¶1`, S325 anchor `§3` -> `§5`, S354 first paragraph, S335/S336 locators (round-55.md Falsify list, lines 205-229). accept-c cannot see it: a wrong locator still resolves to the right row.

Check (from the lane root; prints every entry locator not found in its row's `anchor` cell or its Gate locator — a review-pointer list, not a verdict):

```python
import re, pathlib
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
GATE = pathlib.Path('corpus/lessons/round-56.md').read_text(encoding='utf-8')
E = pathlib.Path('corpus/knowledge/civilizations/kongo-kingdom.md').read_text(encoding='utf-8')
rows = {m.group(1): [c.strip() for c in m.group(0).split('|')]
        for m in re.finditer(r'^\|\s*(S\d{3,})\s*\|.*$', SRC, re.M)}
gloc = {m.group(1): (re.search(r'accessed \d{4}-\d{2}-\d{2}[^—]*—\s*(.*?):\s*["“]', m.group(2)) or [None,''])[1]
        for m in re.finditer(r'^- (\S?\s?)?(S\d{3}) — (.*)$', GATE, re.M)}
def norm(s):
    s = s.lower().replace('¶',' para ').replace('§',' sec ')
    return re.sub(r'\s+',' ', re.sub(r'[^a-z0-9 §¶.\']+',' ', s)).strip()
for pg in re.findall(r'\(([^()]*)\)', E):
    for m in re.finditer(r'S(\d{3})(?:,\s*([^)]*))?', pg):
        sid, loc = 'S'+m.group(1), (m.group(2) or '').strip()
        if loc and norm(loc) not in norm(rows.get(sid,['']*7)[6]+' '+gloc.get(sid,'')):
            print(sid, loc)
```

Demonstration on the round-55 entry: 115 locator pairs checked, 97 anchored, 56 unmatched pointers (S285 "senses I, II, II.2, III", S297 "21.62.2-5", S296 "pp. 154-160", S339 "pp. 182, 193", ...). Spot-checks show most are second citations of an already-opened source at a different place than the row's single anchor — the noise floor of a locator-only grep. Mutation control: for S353, `¶1` anchors, `¶2` does not — the exact shape of the round-55 erratum.

Boundary: the check cannot tell "second locator of an opened source" from "wrong locator"; the falsify wave resolves the pointer list by re-opening. Do not tune the list to zero — 56 pointers on 115 pairs is the honest rate, and rounding it down would have hidden S353.

### FM2 — one case generalised to all Bantu / Africa

Failure: a sentence built on one row's single case is written as a claim about every culture, all Bantu peoples, or Africa. Round 55 fixed scoped versions of this shape ("S311 entry sentence scoped to the Astomi", "Polesye scant-evidence and regional scope", round-55.md Falsify).

Check (probe; every flag is read by a human):

```python
import re, pathlib
E = pathlib.Path('corpus/knowledge/civilizations/kongo-kingdom.md').read_text(encoding='utf-8')
UNIV = re.compile(r"\b(all|every|each|any)\s+(cultures?|peoples?|societies?|bantu|africans?|kingdoms?|languages?|traditions?|humans?)\b|\buniversall?y\b|\bthroughout\s+\w+|\ball of (africa|the bantu|humanity)\b", re.I)
HEDGE = ['by tradition','probably','perhaps','possibly','reportedly','according to','some traditions',
         'almost always','said to','believed to','conjectural','in some','usually','generally','often','many','some']
ATTR = ['according to','says','records','reports','writes','presents','describes','notes','argues','calls']
for n, l in enumerate(E.splitlines(), 1):
    if re.match(r'^\s*-\s*\*\*[RCBHT]\b', l) or l.startswith('**NON-CANON'): continue
    for sent in re.split(r'(?<=[.!?])\s+', l):
        if UNIV.search(sent) and len(re.findall(r'\bS\d{3}\b', sent)) <= 1 \
           and not any(h in sent.lower() for h in HEDGE) \
           and not any(a in sent.lower() for a in ATTR) \
           and not re.match(r'^(rule|decide|name|record|never|do not|date|fix|give|use|keep|file|state)\b', sent.strip(), re.I):
            print(n, sent[:100])
```

Demonstration on the round-55 entry: landed 0 flags (the two raw hits of a looser version were the imperative rule line "give each culture its own monster word" and the hedged "almost always believed", both exempted by the sentence-level guards). Mutated copy (the §1 opener rewritten as "Every culture has monster words that name a function first") flags 1.

Boundary: this is a recall probe, not proof of calibration; a sentence can pass it and still over-read its row. It also cannot see generalisations without universal tokens ("Kongo religion centred on..." written from one witness). The claims file lists the substantive side as review-only; the falsify wave reads for it.

### FM3 — dropped hedges

Failure: the row's page hedges ("by tradition", "probably", "in some traditions", "conjectural") and the landed sentence asserts plainly. Round 55 restored "almost always believed" (S340), "in some traditions" (S338) and "conjectural" (S320) in exactly this class (round-55.md Falsify).

Check (one-directional and honest about it): when the row's own registry bytes carry a hedge token, the entry sentences citing that id must keep hedge or attribution language:

```python
import re, pathlib
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
GATE = pathlib.Path('corpus/lessons/round-56.md').read_text(encoding='utf-8')
E = pathlib.Path('corpus/knowledge/civilizations/kongo-kingdom.md').read_text(encoding='utf-8')
rows = {m.group(1): m.group(0) for m in re.finditer(r'^\|\s*(S\d{3,})\s*\|.*$', SRC, re.M)}
HEDGE = ['by tradition','probably','perhaps','possibly','reportedly','according to','some traditions',
         'almost always','said to','believed to','conjectural','in some','may have','might',
         'for the most part','vary according']
ATTR = ['according to','says','records','reports','writes','presents','describes','notes','argues',
        'quotes','gives','places','files','reads','dates','calls','shows','cites','glosses']
for sid in sorted(set(re.findall(r'\bS\d{3}\b', E))):
    gl = '\n'.join(l for l in GATE.splitlines() if re.match(r'^- .*' + sid + r' — ', l))
    if sid not in rows: continue
    carry = (rows[sid] + ' ' + gl).lower()
    if not any(h in carry for h in HEDGE): continue
    sents = ' '.join(s for l in E.splitlines() for s in re.split(r'(?<=[.!?])\s+', l) if sid in s).lower()
    if not any(h in sents for h in HEDGE) and not any(a in sents for a in ATTR):
        print(sid, 'row hedges:', [h for h in HEDGE if h in carry])
```

Demonstration on the round-55 entry: landed 0 flags (S320's "Bellows calls a conjectural emendation" keeps both the hedge word and the attribution verb; per-sentence scoping is required — line-level matching false-passes because the neighbouring S318 sentence in the same bullet carries "gives" and "places"). Mutated copy (both S320 sentences rewritten to "a Brodvat conjecture") flags S320. An earlier looser token set flagged S333 on landed bytes ("usually" matching generic index prose); the tightened list above was measured at 0 landed flags and still fires.

Boundary (stated because it is the check's real limit): a hedge that lives only on the opened page and never in the row's cells is invisible here — S340's "almost always believed" is carried by the page, not by the row's `teaches` cell, so no registry grep can guard it. The falsify wave's re-opens remain the only guard for that half; this check catches the half the registry itself records.

### FM4 — a catalogue record over-read as a study

Failure: a museum record, an encyclopedia page or a community page is cited in "a study shows" language, borrowing paper-grade authority for a descriptive record. QUALITY criterion 6's logic, applied to kinds.

Check (probe; flags study-language sentences whose cited row is not a paper or dataset):

```python
import re, pathlib
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
E = pathlib.Path('corpus/knowledge/civilizations/kongo-kingdom.md').read_text(encoding='utf-8')
kind = {m.group(1): m.group(2) for m in re.finditer(
    r'^\|\s*(S\d{3,})\s*\|[^|]*\|\s*([a-z]+)\s*\|', SRC, re.M)}
for n, l in enumerate(E.splitlines(), 1):
    for sent in re.split(r'(?<=[.!?])\s+', l):
        if re.search(r'\b(stud(y|ies)|survey|fieldwork)\b', sent, re.I):
            for sid in re.findall(r'\bS\d{3}\b', sent):
                if kind.get(sid) not in ('paper', 'dataset'):
                    print(n, sid, kind.get(sid), sent[:90])
```

Demonstration on the round-55 entry: landed 0 flags (the "2014 study" sentence cites S299, kind paper; the earlier line-level version false-flagged S298/S307/S316 in the same bullets — per-sentence scoping is what makes it clean). Mutated copy (that sentence re-cited to S305, kind docs) flags 1.

Boundary: it reads only the SOURCES `kind` cell; a genuinely analytic book (Wengrow, kind book) is invisible to it and needs the re-open. Keep it as a probe; the strength words "demonstrates/proves/established" deserve the same eyeball wherever they occur.

### FM5 — a publisher blurb used as tier A

Failure: a row whose evidence is a publisher's or platform's description of a work is filed tier A and then cited at full strength. QUALITY criterion 6: descriptions are tier B for substantive claims; tier A is for sources primary or authoritative for the exact scope. Round 55's S256 precedent went the other direction (A -> superseding B row).

Check (row-level over the round's new block; also run it over every cited row):

```python
import re, pathlib
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
BLURB = re.compile(r"publisher'?s? description|book page|press page|about the (book|work|author)|\babstract\b", re.I)
for m in re.finditer(r'^\|\s*(S\d{3,})\s*\|([^|]*\|){2,}\s*$', SRC, re.M):
    c = [x.strip() for x in m.group(0).split('|')]
    if c[4] == 'A' and c[3] in ('book', 'web', 'record') and BLURB.search(c[6] + ' ' + c[7]):
        print(c[0], 'tier=A blurb-shaped:', c[7][:80])
```

Demonstration on the round-55 registry over the entry's 73 cited rows: landed 0 flags — including the eleven kind=book tier=A rows whose "Press" strings are publisher imprints of primary texts (Clarendon Press, Cambridge UP), which a source-cell-only regex would have false-flagged; matching `teaches`+`anchor` is what keeps them out. Mutated copy (S352's tier cell B -> A; its teaches opens "The publisher states Mayor's thesis") flags S352.

Boundary: row-level only. It cannot catch a tier-correct row quoted past its strength in the entry; that stays with the falsify re-opens and the calibration bank.

### FM6 — draft ids left in text

Failure: a seat's placeholder `NEW-<SeatName>-<n>` survives into the landed entry, README row or registry row. Round 55 caught S278/S342 draft ids only by hand (`corpus/lessons/round-55.md:149,151` record the fixes).

Check (grep; the entry, the README index row and the new SOURCES rows must be 0):

```bash
grep -nE '\bNEW-[A-Za-z][A-Za-z0-9]*-[0-9]+\b' \
  corpus/knowledge/civilizations/kongo-kingdom.md corpus/README.md \
  && echo FAIL || echo OK
grep -cE '\bNEW-[A-Za-z][A-Za-z0-9]*-[0-9]+\b' <(sed -n '/^| S359 /,/^| S41[89] /p' corpus/SOURCES.md) | grep -q '^0$' && echo OK || echo FAIL
```

Demonstration on the round-55 bytes: entry 0, README 0, SOURCES 0; the round-55 lesson carries exactly 2 hits, both errata lines describing the fix (`round-55.md:149` "the leftover draft id NEW-ScoutMalagan-4 -> S277", `:151` "the draft id NEW-ScoutMamiWata-1 -> S341") — legitimate record mentions, so the lesson is not in scope of the zero rule; the three C-landed files are. Synthetic string "(NEW-ScoutNzimbuMoney-3, p. 4)" hits.

### FM7 — S-ids outside S359-S418, and block discipline

Already declared: accept-c's RANGE leg (no id below S359, none above S418, exactly one row per cited id, no range notation) plus FLOOR, STATUS, USEDBY. Run it; do not re-derive it. Two adjacent checks the legs do not state, both cheap:

```bash
# rows written inside the block but never cited (round 56 rule: unused ids stay unassigned)
python3 - <<'EOF'
import re, pathlib
src = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
ent = pathlib.Path('corpus/knowledge/civilizations/kongo-kingdom.md').read_text(encoding='utf-8')
block = {m.group(1) for m in re.finditer(r'^\|\s*(S3[5-9]\d|S41[0-8])\s*\|', src, re.M)}
cited = set(re.findall(r'\bS\d{3}\b', ent))
print(sorted(block - cited) or 'OK: no uncited rows in S359-S418')
EOF
```

Demonstration on the round-55 bytes: the entry's 73 distinct ids are all inside its own block S285-S357 (0 outside); the same check against round 56's block flags all 73 — the detector demonstrably fires on out-of-block ids. Range notation: 0 spans (`S\d{3} [–—~…] S?\d{2,3}` shapes from accept-c.py:96). Uncited-block-row check: flags S358 (written, queued, uncited — permitted in round 55 as a record-unit row, forbidden in round 56 where "ids of the block C leaves unused stay unassigned", claims.json export_rule).

### FM8 — Gate Grounds differing from the registry teaches cell

Already declared, with a sequencing trap. O lands the html-entity class in `tools/check-gate-quotes.py`; after landing, `python3 -B tools/check-gate-quotes.py corpus/lessons/round-56.md` must print nothing and exit 0, and the same command on `corpus/lessons/round-55.md` must print exactly the 16 pinned html-entity pairs and exit 1 (claims O, ENTITY/NOFALSE/EXIT legs). The trap: today's pre-O checker prints `GATE_QUOTES: 0 findings`, exit 0 on round-55.md — a green run before O lands proves nothing about entities. The L1 must run the Gate check only with O's tool landed, or cross-check with the byte comparison below.

Independent byte comparison (reproduces the round-55 closure's §3 result exactly: 74 rows, 68 raw-equal, 6 entity-only, decode fixes all six — S288, S305, S326, S341, S343, S348):

```python
import re, html, pathlib
G = pathlib.Path('corpus/lessons/round-56.md').read_text(encoding='utf-8')
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
rows = {m.group(1): m.group(0) for m in re.finditer(r'^\|\s*(S\d{3,})\s*\|.*$', SRC, re.M)}
def strip_q(s):
    s = re.sub(r'["“”«»\']', '', s)
    return re.sub(r'[\s.]+$', '', s).strip()
bad = []
for m in re.finditer(r'^- (\S?\s?)?(S\d{3}) — (.*)$',
                     re.search(r'^## Gate$(.*?)(?=^## )', G, re.M | re.S).group(1), re.M):
    sid = m.group(2)
    g = re.search(r'Grounds:\s*(.*?)(?:\.\s*Seat:.*|\s*Seat:.*)?$', m.group(3))
    if not g or sid not in rows: continue
    t = re.search(r'\|\s*' + sid + r'\s*\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|([^|]*)\|', rows[sid]).group(1)
    if strip_q(g.group(1)) != strip_q(t): bad.append((sid, 'raw'))
    elif strip_q(html.unescape(g.group(1))) != strip_q(html.unescape(t)): bad.append((sid, 'entity-only'))
print(bad or 'OK: every Grounds equals its teaches cell (after decoding)')
```

The two extraction rules that make it exact, both learned by measurement: cut the Grounds at ` Seat:` (the tail otherwise breaks all 74 comparisons), and unescape before stripping quotes (`&quot;` survives quote-stripping otherwise).

### FM9 — HTML character references in the landed bytes

O covers the lesson's Gate rows. The entry and the new registry rows are separate surfaces; round 55's leak was 16 entities into its Gate, and QUALITY round rules require plain UTF-8. Check:

```bash
grep -nE '&(#[0-9]+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]{1,31});' \
  corpus/knowledge/civilizations/kongo-kingdom.md && echo FAIL || echo OK
python3 - <<'EOF'
import re, pathlib
src = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8').splitlines()
for n, l in enumerate(src, 1):
    m = re.match(r'^\|\s*(S3[5-9]\d|S41[0-8])\s*\|', l)
    if m and re.search(r'&(#[0-9]+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]{1,31});', l):
        print(n, m.group(1))
EOF
```

Demonstration on the round-55 bytes: the entry carries 0 entities; `corpus/SOURCES.md` carries 11, all in pre-S359 rows — S246 (`:275`, source cell self-declaring "title field as served: numeric entities"), S320 (`:349`) and S332 (`:361`, `&#124;` line-separators inside verbatim quotes). Those are served-text preservations, not leaks; the allow-list rule for round 56 is therefore: new-block rows and the entry decode to plain UTF-8, and an entity survives only where the cell itself says it quotes the page as served (S246 precedent). Synthetic `&ldquo;`/`&rdquo;` hits.

### FM10 — entry-local `[S##]` keys colliding with registry ids

Round-55 Frontier class: `haudenosaunee.md` cites its own `[S95]` key, which collides in shape with registry id S095 and would poison every `\bS\d{3}\b` sweep. One grep before landing:

```bash
grep -nE '\[S[0-9]{1,3}\]' corpus/knowledge/civilizations/kongo-kingdom.md && echo FAIL || echo OK
```

Demonstration on the round-55 entry: landed 0; a mutated `(S341, Introduction page)` -> `[S41]` hits.

### Shape and calibration reminders that carry over

- Length: `wc -l corpus/knowledge/civilizations/kongo-kingdom.md` at most 230 (claim C). The round-55 entry is 188 lines, so the cap is live, not nominal.
- Head: the eight keys in exact order `topic, gap filled, sources, couples, source, verified-at, recheck, scope` (round-50 contract §2.3). Measured on the round-55 entry: exact match. Reuse the contract's §2.9-A checker with the Kongo path.
- Register words in `- topic:`: the round-56 topic must carry kongo/kikongo/mbanza as whole words, or every future freshness probe misses the entry (contract §2.3 field 1; claims list the topic as review-only). `grep -ciE 'kongo' <entry>` on the topic line only.
- Calibration on first use (QUALITY criterion 2; claims review-only): every sentence containing "cosmogram" must carry attribution or a hedge word, and the calibration bank must file the contested cosmogram reading explicitly. `grep -n 'cosmogram' <entry>` then eyeball each hit; a bare "minkisi are arranged as a cosmogram" with no interpreter named is the defect.
- Canon hygiene (criterion 5): the handoff section names what lore-shokunin receives; claims list it review-only; the round-50 contract §2.4 item 9 wording is the model.
- Records after C: routed registry fixes below S359 and the lesson land in the records commit, which must keep ACCESS and the census green (claims.json records_not_claims note). S256-style corrections are superseding rows or logged cell edits, never silent in-place rewrites (QUALITY criterion 6; round-55.md Falsify, ReviewRoutedFixes55).
- Receipts name their revision (round-55 spot-check routed defect 3): every telemetry line the L1 writes carries the commit hash it measured.

## 3. Order of operations for the L1

1. Integrate seat drafts; apply FM1's pointer list, FM2-FM5 probes and the FM6-FM10 greps before the entry lands; iterate until each is clean or the residue is an explicitly accepted review pointer.
2. Land O first in the acceptance sequence, then run `tools/check-gate-quotes.py` on round-55.md (expect the 16 pinned entity pairs, exit 1) and on round-56.md (expect nothing, exit 0).
3. Run `python3 -B reports/round-56/accept-c.py` at the tip; all seven legs must pass (FLOOR at least 20 distinct ids, RANGE inside S359-S418, STATUS mined, USEDBY whole-item).
4. Write the round-56 lesson Gate with the `- S0nn — URL — accessed 2026-10-22 — locator: "quote". Grounds: <teaches-echo>. Seat: <name>.` shape, then re-run the Gate check — the Grounds field is the teaches cell's echo, and R55-M1's 220-character truncation shape is what truncated-grounds now catches.
5. Records commit last: routed registry fixes, lesson, SCORECARD append-only.

## 4. Residual risk and verification gaps

- FM1's 56-pointer noise floor on round-55 bytes means wrong-locator coverage is a wave of re-opens, not a green line; the check only aims it.
- FM3 is one-directional by construction: hedges carried only by the page (S340's "almost always") are invisible to any registry-side grep. The falsify wave's re-opens are the guard; budget them.
- FM2 and FM4 are recall probes with human read-out; a generalisation without universal tokens and a study-verb without "study" both pass. No mechanical check was built for them, deliberately.
- FM5 is row-level; a correctly-tiered row quoted past its strength still needs the re-open.
- The pre-O checker's green run on round-55.md (measured this session: 0 findings, exit 0) shows acceptance order matters; running the Gate leg before O lands would certify nothing.
- No external source was opened by this seat; every demonstration is over landed lane bytes. Nothing here verifies the Kongo sources themselves — that is the source seats' and falsify wave's work.
- No installs or tool updates were made (tooling record: system python3 only, lane tools in read mode).
