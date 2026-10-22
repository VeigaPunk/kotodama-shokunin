# ReviewEntryContract — round 55, claim C: monsters-hybrid-beings entry contract attack

- Seat: `KotodamaR55.ReviewEntryContract` (leaf; no delegation, no background jobs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, main, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`.
- Read-only everywhere except this report. Every check ran in memory or read-only against the working tree; demonstrations run against `corpus/knowledge/culture-material/masks-masquerade.md` (the round-54 entry) and `corpus/lessons/round-54.md`. No lane file was edited, staged or created except this report.
- Axes judged: coverage, calibration.

## 0. Result

- **The round-54 residual evidence names six recurring failure shapes**, all documented with re-opened sources: wrong locators (9 confirmed findings), over-reads including dropped hedges and one-case generalisation (8), a doubled-locator Gate shape (13 lines), truncated Gate grounds (17 lines), plus one landed `NEW-*` draft id my check 5 found live at `corpus/SOURCES.md:307`.
- **A mechanical sieve exists for each of the six named modes** (§2). Three checks fire on real defects or historical defect shapes replayed against the live masks file; two reproduce the closure's exact counts on `corpus/lessons/round-54.md` (17 truncated grounds, 13 doubled locators). The catalogue-over-read check needs an attribution-verb allowlist; the hedge check produces an adjudication list, not a verdict.
- **Three defect shapes are invisible at registry level** — transposed locators (S270 "sentences 12 and 8"), off-by-one paragraph counts against the row (S266 ¶3 vs ¶4), and semantic over-read of carried text (S241 "silent" wearers, S243 "not portraits", S247 "for the rest of the year"). The claims file's review_only clause assigns exactly this to the falsify wave; the sieve only bounds it (§3).
- **One live defect found while demonstrating check 5:** `corpus/SOURCES.md:307`, the S278 Horniman row's scope cell still reads "Its disposal sentence disagrees with NEW-ScoutMalagan-4" — a draft id never substituted (idmap says NEW-ScoutMalagan-4 → S277). Routed as a fix candidate for the L1 (§3).

## 1. Evidence base read

- `.ufo/waves/round-50/build/ReviewEntryContract.md` §2 — the eight-field head + body contract, §2.9 mechanical checker pattern, D2 (whole-word evidence probes), D5 (separability text discipline).
- `.ufo/waves/round-54/residual/ReviewRows*.md` (all six slices) — per-row verdicts below.
- `.ufo/waves/round-54/residual/CriticClaimC.md` — clause-level findings (generalisation, restricted traditions, duplicate authority).
- `corpus/lessons/round-54-verifier-spotcheck.md` §5 — routed defects 1 and 2 (Gate grounds truncated ×17; doubled locator ×13), defect 4 (carried registry items, five gate-quote escape classes).
- `reports/round-55/claims.json` — claim C legs (SET, SWEEP, FLOOR ≥20 distinct, RANGE ≥S285/one row/no range notation, STATUS mined, USEDBY, ACCESS), red controls (RED-FLOOR: S304 written as S303 = a substitution slip).
- `corpus/knowledge/culture-material/masks-masquerade.md` (152 lines, the demonstration target), `corpus/SOURCES.md` rows S239–S284, `tools/check-gate-quotes.py` (at base it has **neither** `doubled-locator` nor `truncated-grounds`; grep for both terms returns nothing — claim O lands them this round, so pre-O the greps in §2.6/§2.7 are the check).

## 2. The checklist — failure mode → mechanical check → demonstration

Six named modes, ordered by integration sequence: substitute ids (C5), then prose checks (C2, C3, C4), then locators (C1), then the lesson's Gate (C6a, C6b).

### C1 — Wrong locators (entry `Snnn, <locator>` vs the row's own cells)

**Round-54 evidence.** S251 cited twice as `"Body, ¶4"` — the page has no "Body" section; real locator was `"Watch a Cham Dance", ¶2` (ReviewRows247to254:12–13). S245 cited `"body"` for a sentence that lives only in `Abstract, ¶1` (ReviewRows239to246, L87). S261 cited `fig. 325 caption`; the conjunction is verbatim in fig. 324's caption (ReviewRows255to262). S266 `¶3` → real `¶4` (ReviewRows263to270). S270 transposed sentence numbers (ReviewRows263to270, L91). S266's entry ¶3 also *contradicted the row's own ¶2 counting convention* — the registry-visible sub-shape.

**Mechanical check** (run from lane root, entry path as argv[1]):

```python
# locators.py — fires on every cited row whose locator shares no section word
# with the row's anchor+source+scope cells. Every hit = adjudicate:
# either fix the entry locator or fix the row via a superseding row.
import re, sys, pathlib
ENT = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
rows = {}
for ln in SRC.splitlines():
    m = re.match(r'^\| *(S\d{3}) *\|', ln)
    if m:
        c = [x.strip() for x in ln.split('|')[1:-1]]
        rows[c[0]] = ' '.join(c[1:7]).lower()   # source kind tier scope anchor teaches
GENERIC = {'the','and','for','with','section','paragraph','para','sentences','sentence',
           'opening','record','page','text','quote','line','lines','abstract','sense',
           'senses','above','first','second','third','final'}
head_end = next(i for i,l in enumerate(ENT.splitlines()) if l.startswith('## '))
for i, line in enumerate(ENT.splitlines(), 1):
    if i <= head_end or line.startswith('| '):
        continue                                  # head fields and table rows only
    for m in re.finditer(r'\((S\d{3}),\s*([^)]+)\)', line):
        sid, loc = m.groups()
        if sid not in rows:
            print('L%d %s: NO ROW' % (i, sid)); continue
        words = [w for w in re.findall(r"[A-Za-z'’\-]{3,}", loc) if w.lower() not in GENERIC]
        if words and not any(w.lower() in rows[sid] for w in words):
            print('L%d %s locator %r shares no word with row cells' % (i, sid, loc))
```

**Demonstration on masks-masquerade.md** (post-fix bytes, 152 lines): 2 adjudicable hits on the landed text — `"Iconographic meaning"` (S246, L24; the round-54 reviewer confirmed the entry locator content-correct, so this is a row-anchor gap to route, not an entry fix) and `"Notes p. 65"`-style hits for S257 (L80; anchor omits the Notes page). Replaying the historical defect `(S251, "Watch a Cham Dance", ¶2)` → `(S251, Body, ¶4)` in memory: **does not fire** — S251's scope cell contains "what the masks demand of a body", so word-overlap is blind to plausible-sounding section names. **Verdict: the check's value is a must-adjudicate list over row anchors and entry locators together, not a locator-verifier.** The S251-class defect is only visible against the page (§3).

### C2 — One case generalised to "some cultures" / "is normal"

**Round-54 evidence.** `:65` "a closed portion is normal" from one Pingxiang fieldworker's restriction (S249 p. 99) — fixed to "is possible" (CriticClaimC §2d). `:53` "a portrait cannot [be reproduced]" from one V&A mould (S253), contradicted by the entry's own §7 — deleted. The literal phrases "some communities" and "masks everywhere" never appeared; the generalisers were *predicates*, so the check is a phrase list plus a blanket-claim sentence test.

**Mechanical check:**

```sh
grep -nE '\b(some cultures|some communities|some traditions|most cultures|many cultures|all cultures|every culture|cultures everywhere|the world over|in every society|is normal)\b' corpus/knowledge/myth-symbol/monsters-hybrid-beings.md
```

Plus the one-case test: any hit whose sentence carries exactly **one** `(Snnn, …)` citation is a likely one-case generalisation — a single `awk`/`grep` pass on the same file showing the citing part suffices; the L1 reads each hit.

**Demonstration on masks:** exactly one hit — L141 `[## 12. Calibration bank] "- **R — "masks are universal and mean the same everywhere."**…"`, i.e. an R-coded trap claim *inside quotation marks in the Calibration bank*. So the check needs that single allowlist (quoted claims in the Calibration section are the trap inventory, not assertions). Replaying `a closed portion is normal` at L65 fires under `## 4. Access rules` — caught.

### C3 — Dropped hedges ("sometimes", "usually", "is said to")

**Round-54 evidence.** S245 "usually incorporates miniature representations" → entry dropped "usually" (ReviewRows239to246, L104). S261 "usually an old sowei mask" → entry categorical (ReviewRows255to262, L110). S253 "would have been moulded" → "was moulded" (ReviewRows247to254, finding 18). S262 "sometimes in an enclosed area" → entry added "only" (CriticClaimC, Sande). All four were restored at `58b2fae`/`e17bc2b`.

**Mechanical check** (adjudication list — a hit is "the row's anchor carries a hedge the citing line does not"; the L1 re-reads that sentence, it is not automatically a defect):

```python
# hedges.py
import re, sys, pathlib
ENT = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
rows = {}
for ln in SRC.splitlines():
    m = re.match(r'^\| *(S\d{3}) *\|', ln)
    if m:
        c = [x.strip() for x in ln.split('|')[1:-1]]
        rows[c[0]] = c[5]                          # anchor cell
H = r"\b(usually|sometimes|often|typically|generally|mostly|probably|apparently|reportedly|said to|believed to)\b"
head_end = next(i for i,l in enumerate(ENT) if l.startswith('## '))
for i, line in enumerate(ENT, 1):
    if i <= head_end or line.startswith('| '):
        continue
    for m in re.finditer(r'\((S\d{3}),\s*([^)]+)\)', line):
        r = rows.get(m.group(1))
        if not r: continue
        miss = sorted({h for h in re.findall(H, r, re.I)} 
                      - {h for h in re.findall(H, line, re.I)})
        if miss: print('L%d %s hedge in row anchor missing on entry line: %s' % (i, m.group(1), miss))
```
**Demonstration on masks:** 9 candidate hits on the landed file (e.g. L64 S250 "believed to" — a hedge the anchor carries for a *different* section than the one cited; the entry's attributive "states" does the work). After adjudication all 9 are carried. Replaying the defect — deleting "usually" from the gonde line (L109) — fires exactly: `L109 S261 hedge in row anchor missing on entry line: ['usually']`. **The check converts a semantic problem into a small re-read list; the landed masks file's own residual history (4 real hedge drops among ~46 rows) is the base rate to expect.**

### C4 — A catalogue record over-read as a study

**Round-54 evidence.** B-code calibration line: "A holding museum's record is authoritative for its own object's data, not for a tradition's meaning" (`masks-masquerade.md:144`). The near-misses it guards: S273 NAM "intention to depict" read as the museum's own reading (carried, attributed); S262 Phillips behind a "holding-institution" framing where only the Agnes Etherington part (S260) qualified — the scholar-sourced remainder needed attributive verbs (CriticClaimC §2c). The mode is: `kind=docs` or `kind=community` row cited with the page's content asserted directly.

**Mechanical check** (run from lane root, entry path as argv[1]):

```python
# attribution.py — docs/community rows cited without an attribution verb
import re, sys, pathlib
ENT = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
SRC = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
kind = {}
for ln in SRC.splitlines():
    m = re.match(r'^\| *(S\d{3}) *\|', ln)
    if m:
        c = [x.strip() for x in ln.split('|')[1:-1]]
        kind[c[0]] = c[2]
ATTR = re.compile(r"\b(states?|records?|catalogues?|lists?|describes?|labels?|reports?|says?|notes?|reads?|according to|per its|writes?|marks|gives|shows?|calls?|files|dates|measures|found|argues?|suggests?)\b", re.I)
head_end = next(i for i,l in enumerate(ENT) if l.startswith('## '))
for i, line in enumerate(ENT, 1):
    if i <= head_end or line.startswith('| '):
        continue
    for m in re.finditer(r'\((S\d{3}),\s*([^)]+)\)', line):
        if kind.get(m.group(1)) in ('docs','community') and not ATTR.search(line):
            print('L%d %s kind=%s cited with no attribution verb' % (i, m.group(1), kind[m.group(1)]))
```

**Demonstration on masks:** 0 hits on the landed file — every `docs`/`community` citation is attributed ("The Oslo museum states…", "The Rubin Museum states…", "states that", "records that", "per its catalogue text" pattern). Mutating L51 to assert "The Garā Yakā's presence brings success, purification and prosperity (S250, Kōlam Theatre section)" (attribution dropped) fires: `L51 S250 kind=docs cited with no attribution verb`. For monsters: bestiary catalogue pages, museum object records (Sphinx/Chimera relief, lacquer Chimera disk), and community statements are exactly the `docs`/`community` rows where this bites.

### C5 — Draft ids left in text

**Round-54 evidence.** Seat drafts wrote `NEW-ScoutMalagan-4` etc.; the integrator substituted via `/fast/scratch/hyaku/kotodama-r54-a2/idmap.tsv` (format `Snnn←NEW-<Seat>-<n>`, per ReviewRows271to278:5). The substitution missed a registry cell: **S278's scope cell still reads "Its disposal sentence disagrees with NEW-ScoutMalagan-4" — live at `corpus/SOURCES.md:307` right now** (the id it should name is S277). Neither the round-54 residuals nor the closure caught it; my check 5 did. Claims' RED-FLOOR control (S304 written as S303) is the same family: an off-by-one or missed substitution inside the idmap.

**Mechanical checks:**

```sh
# any draft id left anywhere in lands or frontier:
grep -rnE '\bNEW-[A-Z][A-Za-z]+-[0-9]+' corpus/knowledge corpus/SOURCES.md corpus/README.md corpus/lessons/round-55.md
# every S-id cited by the entry is exactly the set of rows that name it in used-by
# (the idmap-closure check; needs idmap.tsv at reports/round-55/ or scratch):
python3 - <<'PY'
import re, pathlib
ent = pathlib.Path('corpus/knowledge/myth-symbol/monsters-hybrid-beings.md').read_text(encoding='utf-8')
src = pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8')
rows = {m.group(1): m.group(0) for m in re.finditer(r'^\| S\d{3} .*$', src, re.M)}
for sid in sorted(set(re.findall(r'\bS\d{3}\b', ent))):
    r = rows.get(sid)
    print(sid, 'no-row' if r is None else ('used-by-missing' if 'monsters-hybrid-beings.md' not in r else 'ok'))
PY
```

**Demonstration:** `grep -nE '\bNEW-[A-Z][A-Za-z]+-[0-9]+'` on the entry → 0 hits; on `corpus/SOURCES.md` → **1 hit, line 307** (the real landed defect quoted above). Note the `-r` scope must include SOURCES.md and the round lesson — the round-54 miss happened because draft-id sweeps targeted the entry, not row cells. Second, weaker shape guard: `grep -nE 'NEW-' corpus/SOURCES.md` (loose) finds the same line and would also catch `new-` URL slugs; the tight pattern with the `-<n>` suffix is the right one.

### C6 — Gate grounds cut mid-sentence and doubled locators (the round lesson's `## Gate`)

**Round-54 evidence (closure §5, re-measured by me now).** Truncated grounds: 17 of 46 Gate lines end mid-word before `. Seat:` (S241 "…is silent and a." etc.) — my re-run of the closure regex reproduces exactly 17 on `corpus/lessons/round-54.md`. Doubled locator: 13 lines repeat the section name as a quoted span before the real quote (`'Transformations', ¶1: "Transformations", ¶1: "…"`) — my span rule reproduces exactly 13 (first hits at lines 23, 24, 27). Both defects made "the record of *why* each source was admitted partly unreadable" (closure §4). Claim O lands `doubled-locator` and `truncated-grounds` classes in `tools/check-gate-quotes.py` this round — **but at base the tool has neither class** (grep verified), so until O lands the greps below are the check.

**Mechanical checks on `corpus/lessons/round-55.md` before landing the lesson:**

```sh
# truncated grounds: any Gate line ending a lowercase word + period before . Seat:
python3 - <<'PY'
import re, pathlib
t = pathlib.Path('corpus/lessons/round-55.md').read_text(encoding='utf-8')
gate = [l for l in t.split('## Gate')[1].split('## ')[0].splitlines() if l.startswith('- S')]
bad = [l[:80] for l in gate if re.search(r'[a-z,;] ?\. Seat:', l)]
print(len(bad), 'truncated grounds'); [print(' ', b) for b in bad]
PY
```

```python
# doubled locator: any quoted span whose text occurs verbatim earlier in its line
import re
def doubled(line):
    for m in re.finditer(r'“[^“”\n]*”|"[^"\n]*"', line):
        if m.group(0)[1:-1] in line[:m.start()]:
            return m.group(0)
    return None
```

**Demonstration:** on `corpus/lessons/round-54.md`'s 46 Gate lines — truncated regex: **17 hits** (closure counted 17; list `[25, 26, 28, 32, …]`); doubled-locator span rule: **13 hits** (closure counted 13; first three `'Transformations'`, `'The African Masking Configuration'`, `'Nanfeng Nuo Dance Masks'`). If O lands first, `python3 -B tools/check-gate-quotes.py corpus/lessons/round-55.md` reports both as named classes. For the entry itself the analogous defect is a citation dropped mid-clause — same regex minus `Seat:` gives the entry-side sanity pass: `grep -nE '[a-z,;] ?\. *\(S[0-9]' <entry>` (expect 0).

## 3. What the sieve cannot see — and the live defect found

- **Ordinal truth is page-level, not registry-level.** S270's transposed "sentences 12 and 8" and S266's ¶3-vs-¶4 are only provable by re-opening the page; row anchors are samples, not ordinal maps (my ordinal cross-check against row cells produced 15 false positives on the landed file and I discarded it). The falsify wave owns this; the L1's pre-landing lever is the seat draft's `quotes:` list — every quoted span in the entry that is *not* in its row's anchor must be re-opened before landing (the "quote coverage" list; on masks ~59 such spans exist because content quotes legitimately outnumber anchor samples — an adjudication list, not a verdict).
- **Semantic over-read of a correctly-located quote** is page-level: S241 "the masked figures were silent" (page shows them with no lines, never states silence — ReviewRows239to246), S243 "not portraits of individuals" (the entry's own gloss; the roster includes heroic individuals), S247 "for the rest of the year" (entailed only by combining p. 476's calendar). No regex catches these; they are why the `review_only` clause says each sentence is carried "at the strength stated".
- **Duplicate authority** (CriticClaimC §2b): S265 created a second citation identity for the 1995 Grand Council policy the owner already cites as `[S95]` (a pointer that resolves to a different registry row). Mechanical approximation: `grep -nE '\[\[?S[0-9]+\]?\]' corpus/knowledge/civilizations/*.md` plus reading the pointed `path:line` whenever the entry cites a community statement — check the owner file's own `Snn` tokens resolve and do not name the same document under another id.
- **LIVE DEFECT — `corpus/SOURCES.md:307`.** The S278 Horniman row's scope cell: "Its disposal sentence disagrees with NEW-ScoutMalagan-4 and should be reported as a disagreement, not a rule." Per the round-54 idmap (`ReviewRows271to278.md:5`), `NEW-ScoutMalagan-4` → S277 (Tassignon/Fondation Gandur kavat essay), and the landed entry does exactly what the cell prescribes (`masks-masquerade.md:109` "the sources disagree, so decide each mask type's fate separately" citing S275–S278). So the intended fix is a superseding row or erratum changing only that cell's `NEW-ScoutMalagan-4` → `S277`; this matches the claims file's "routed registry fixes in corpus/SOURCES.md rows below S285" (records-not-claims). Not verified against a routing list for round 55 — no `.ufo/waves/round-55` file mentions it.
- **Substitution-slip companion check** (RED-FLOOR family): after the L1 assigns S285+, run `comm -3 <(grep -oE 'S[0-9]{3}' entry | sort -u) <(grep -oE '\| S[0-9]{3} ' corpus/SOURCES.md | awk '{print $2}' | sort -u)` scoped to the new rows, plus verify every `NEW-*` id in the seat drafts appears exactly once in the idmap and exactly once as an S-id in the entry. The entry must not cite any id below S285 (RANGE leg) — `grep -nE '\bS(0|1|2)[0-9]{2}\b' <entry>` after substitution must show only `S2[89][0-9]`-safe patterns (i.e., ≥S285).

## 4. Contract items carried forward from round-50 §2 (applied to this claim)

- Eight-field head `topic, gap filled, sources, couples, source, verified-at, recheck, scope`; last H2 `Scope`, preceded by `Recheck`; no H3+; `wc -l` ≤ **230** (this round's bound).
- `- topic:` single line containing the register words a future freshness probe would grep (`monster`, `hybrid`, `bestiary`, `chimera`, `composite` as whole words — D2: use `\b`-bounded probes in the gap evidence).
- `- couples:` entries partition-labelled and basename-resolvable (`basename-couples-resolver.py`).
- SOURCES rows: 11 columns, `kind` ∈ observed set, `tier` per QUALITY criterion 6 (`community` never A; publisher description = B), `status=mined` at landing, `used-by` names the entry, `opened=2026-10-22`, quote ≤25 words verbatim.
- README edits: `## myth-symbol/` count, index row with **byte-equal** topic (`topic_of()` vs row text — the SWEEP leg's `topic_mismatch`), `Total knowledge entries: 231`, footer counts, one unique non-increasing `revision:` label with non-blank body, appended re-measured paragraph. The RED-COUNT/RED-SWEEP-EXIT controls exist precisely because a 232-drift can hide under a passing sweep — so verify the footer literal, not only exit 0.
- No `Snnn–Snnn` range notation in the entry (RANGE leg; the round-53 model's `S134–S183` idiom is banned here).
- No placeholders/TODO; NON-CANON worked example; calibration bank uses R/C/B/H/T registry codes.

## 5. Counts, unrun checks, tooling

- Checks demonstrated: C1 (entry locators vs row cells; 2 adjudicable hits on landed file, historical S251 shape uncatchable), C2 (1 allowlisted hit; mutation fires), C3 (9 adjudication hits; mutation fires), C4 (0 hits; mutation fires), C5 (0 entry hits; **1 live SOURCES.md:307 hit**), C6a truncated grounds (17 on round-54 lesson — matches closure), C6b doubled locator (13 — matches closure; synthetic line fires).
- Unrun: `accept-c.py`/`accept-o.py` (no lands exist yet); `sweep.py`; page re-opens (out of scope — falsify wave's job); `basename-couples-resolver.py` on a file that does not exist yet; the whole-entry head checker (§2.9-A pattern) — reusable but not re-run since no entry exists.
- No tool installs (host-wide pacman pause observed; used system python3/curl-free read paths only). All checks ran from `eval` in memory or as read-only greps; nothing written except this report.
- Residual risk statement: the sieve bounds *integration mechanics* (ids, locators, hedges, attribution, Gate shape); it does not bound *page truth* (carried strength, ordinal correctness, over-read). Round-54 found 9 wrong-locator + 8 over-read findings across the row slices and 4 review-clause failures — expect the same order of latent defects among the seat drafts this round; the falsify wave must re-open pages, the sieve only makes its findings non-recurring.
