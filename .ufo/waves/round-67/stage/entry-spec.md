# Entry spec — `corpus/knowledge/culture-material/medicine-healing-codes.md` (claim C, drafting plan)

Status: pre-data design draft for integration. This is **not** the entry and contains no claim
text. Every `(S###)` bullet in the entry must come from that row's fragment
(`.ufo/waves/round-67/rows/ScoutRow*/row-S<ID>.txt`, field `BULLET=`); this file fixes the
skeleton, the section each row lands in, the clause angle, and the one-way boundaries. Nothing
here may be pasted as evidence: only `reports/round-67/accept-c.py` on a materialized clone at
the lands commit decides the claim.

## 0. Constraints read from the frozen instrument (accept-c.py, revision 0)

| leg | what it forces on the entry text |
|---|---|
| FILE | exactly 1 `# ` H1; **0** `### `; `## ` count ≤ 16; total lines ≤ 250; one non-empty `- topic:` line |
| ONEID | every `\((S\d{3,})\)` occurrence must be one of S805–S828, **and each exactly once**; no other registry id anywhere in the file (metadata, section leads, boundaries, handoff) |
| RESTATE | exactly one line per id carries `(S###)`; that line must hold ≥ 3 content words from the row's **first quoted span** in order, in-order coverage of the `teaches` cell **< 0.80**, ≥ 1 content word absent from `teaches`; row-side: `teaches` ≥ 4 content words and < 0.80 in-order echo of the quote |
| TOPIC | the entry's `- topic:` text and the README row must agree. `accept-c.py` takes the **first** `- topic:` physical line, strips it, and substring-tests it in the first `- ` line containing the basename; `sweep.py` compares the row to the entry's topic with **continuations space-joined and equality** (`ROW_RE = ^- \`([^\`]+\.md)\` — (.*)$`, space em dash space, one physical line). The row must use the **backticked basename** — the wave-prompt shorthand with the full path is invisible to `ROW_RE` and fails SWEEP as a missing row. Source of truth: `stage/readme-row.txt`; if the entry's topic changes, regenerate that row from the entry, never the reverse. |
| ROWS | row-side only: 11 cells, `kind` in {spec,docs,paper,code,tool,dataset,talk,book,community,own-work}, tier A/B, status `mined`, opened `2026-10-24`, used-by the exact entry path, live URL + same-page `web.archive.org/web/<14-digit>id_/…` capture |
| APPEND / CAPTURE / HOSTS / LINK | row-side only; APPEND permits additions S805–S828 (+ S801–S804) and in-place flips of the status/recheck/used-by cells only (declared exception: S753's used-by). **Any literal `|` inside a cell breaks `cells()` and fails ROWS** |
| NOHARM | `git diff BASE -- corpus/knowledge` shows only this new entry |
| SWEEP | README rows == files, 0 topic mismatches; after landing, culture-material 33 → 34 and total 240 → 241, footer totals likewise |
| line budget | the skeleton below is ≈79 physical lines (H1 + 5 metadata + 10 H2 + 8 leads + 8 class bullets + 24 cited bullets + 12 boundary/handoff bullets + 11 blanks), well under the 250-line cap |

Measured base facts (this seat, read-only, base `ad5b52b0`):
`git ls-tree -r --name-only <base> -- corpus/knowledge | wc -l` → **240**;
culture-material → **33**; `git show <base>:corpus/SOURCES.md | grep -cE '^\| *S[0-9]+'` → **724**
rows, tail ids S797–S800; S801–S804 absent; the claim-C filename census on the base tree → **0**.
Note: `rows/ScoutGapMed/gap.md` says "Culture-material has 34 files" — the base tree has 33; the
number does not feed any counter leg, but do not copy it into the README revision note.

## 1. Register map — what this entry owns

Owned register: **the code a culture writes onto sickness** — what illness is said to be, who is
allowed to name it, who treats it and under what warrant, where treatment happens, what is
administered or worn, how the body is acted on, how techniques travel, and what a polity does
when many are sick. The entry owns the *healing register*; it does not own the body's hygiene,
the smell of prophylaxis, the purity boundary, or the corpse's disposal.

| slot this entry owns | the partial owner that keeps its ground (one-way, named once in §9) |
|---|---|
| aetiology, diagnosis as a claim, practitioner roles, institutions of care, materia as therapy, technique, crisis response, the medical text genres | `bathing-and-body-hygiene.md` (bath institution, water/heat, hygiene vs purity, §8 therapy doctrine) |
| materia that is inhaled, burned, worn as scent; the prophylaxis object | `scent-perfume-aromatics-codes.md` (§1–§4, Boundaries) |
| the sick body as a category violation; who counts as pollution | `myth-symbol/purity-pollution-boundary-systems.md` (§2, §5, §7) |
| disposal, grave assemblage, monument, mourning economy, the death register | `culture-material/funerary-material-culture.md` (§2–§6) |
| the amulet as an object class and its mechanism | `myth-symbol/amulets-talismans-apotropaic-marks.md` (§4, §6, §9) |
| the shrine, the votive receipt, the incubation archive | `myth-symbol/sacred-topography-pilgrimage.md` (§5) |

Rule: §1 states ownership only. Every neighbour pointer lives in §9, once — the plan deliberately
does not duplicate one-way pointers in two sections.

## 2. Medicine-as-code classes (analytic; one row is cited in exactly one section)

| class | what it encodes | design question the class answers | rows | section |
|---|---|---|---|---|
| A aetiology | what illness *is* | is sickness a body state, a person state, or an intrusion? | S805, S806, S807, S816 | §2 |
| B authority / canon | what warrant names and fixes illness | is authority textual, demonstrated, or licensed? | S811, S808, S812 | §3 |
| C practitioner role | the ladder of who may treat, and its guild | guild member, court servant, ritual specialist, contract worker? | S818, S823, S824 | §4 |
| D institution | the building that owns care | who pays, who is admitted, who is refused? | S810, S809, S822, S825 | §5 |
| E materia | what is administered or worn as therapy | ingested, worn, or performed? | S815, S828, S817 | §6 |
| F technique | how the body is acted on | opened, punctured, or dosed? | S819, S826, S814 | §7 |
| G transmission | how a system crosses a border and is renamed | marked foreign, naturalised, or split elite/folk? | S821, S826 | §7 |
| H crisis | what a polity does when many are ill | isolation, costume, counsel, or procession? | S820, S813, S827 | §8 |

The class table is analytic: S819 sits in B and F, S826 in F and G, S813 in C and H. The **section
assignment is single-valued** (§2–§8 below) because ONEID forbids a second citation of any id.

## 3. Section plan (10 H2; H1 + 5 metadata lines + 7 cited sections + 2 one-way sections)

H1 (draft, one line):
`# Medicine and healing codes — the ailment as a classified sign: theory frames, practitioners, institutions, materia, technique and the crisis response`

Metadata block (one line each, **no parenthesised ids**): `- topic:` (copy the string from
`stage/readme-row.txt` after the em dash — or regenerate that row from the entry if the entry's
topic differs; `sweep.py` equality joins continuation lines, so a wrapped topic is allowed only
if the join reproduces the row byte for byte), `- source:` ("the rows opened this round in
`corpus/SOURCES.md` are the evidence anchors; each inserted claim stays within its cited row"),
`- verified-at:` (**must be filled with the observed accept-c result and the clone/lands used —
never a pre-written PASS**), `- recheck:` ("180 days, per row"), `- scope:` ("reference knowledge
and craft method for the culture-material partition only; decides nothing about any world, names
no canon fact, ends at the handoff").

Cross-seat conflict to resolve before landing: the README seat's proposed topic promises
"**surgical instruments and wound care**" and "**diagnosis, prognosis**", but no claim-C row
covers instruments or wound care (nearest: S823 barber-surgeon guilds, S826 needling) and
diagnosis is only implied by S824's divination role. Because the row must equal the entry topic,
integration must either drop those phrases from both or keep them as deliberate prompt-level
scope and accept that the rows support less than the sentence advertises.

### §1 `## 1. What this entry owns: the healing register as a set of codes`
Lead (one sentence, no id): the owned object is the code written onto sickness, not the biology
of disease; each following section fills one code class from one registry row apiece.
Non-cited bullets: the eight class slots A–H, one line each, phrased as the design question the
class answers. Last line: "the partial owners and their retained ground are named once, in §9".

### §2 `## 2. Aetiology: four theory frames` — S805, S806, S807, S816
Bullet order: humoral corpus (S805) · doshic constitution (S806) · qi/meridian topography (S807)
· the four-tantra canon (S816). Each bullet names its frame and the diagnostic vocabulary it
creates. **Guard:** keep the four frames separate — no bullet may blend humoral with doshic or
fold Tibetan into Ayurvedic; S812 (Galen) is *not* here.

### §3 `## 3. Canon, commentary and the medical book` — S811, S808, S812
Bullet order: case/recipe papyri as a written archive (S811) · the canon as a portable curriculum
(S808) · system-building that fixes doctrine as authority (S812). **Guard:** S808 owns the book's
travel; S812 owns the system, not the book; neither may restate §2's theory content.

### §4 `## 4. Practitioners, guilds and licensing` — S818, S823, S824
Bullet order: apothecary shop + guild regulation of stock (S818) · the surgeon/barber-surgeon
split as a class code (S823) · the divining healer's social role (S824). **Guard:** S818 and
S823 are two different guilds — do not generalise one into "the medical guild"; S824 carries the
living-tradition restraint (§9, last bullet) in its wording.

### §5 `## 5. Institutions of care` — S810, S809, S822, S825
Bullet order: the army's own hospital as a readiness institution (S810) · the monastic infirmary
as a duty with a pharmacy wing (S809) · the endowed hospital with wards and staff (S822) · the
temple cure by incubation (S825). **Guard:** religious doctrine stays with the cult entries; S825
cites the *therapeutic procedure*, not the votive economy or the archive (§9).

### §6 `## 6. Materia medica and protective objects` — S815, S828, S817
Bullet order: the illustrated herbal that fixes materia in a colonial frame (S815) · the amulet
as something a healer *prescribes* (S828) · the lodge/sweat therapy as a supervised collective
ordeal (S817). **Guard:** the amulet entry owns the object and its mechanism; the bathing entry
owns the sweat bath as a bathing regime and the hot-spring therapy doctrine.

### §7 `## 7. Technique and its transmission: opening, needling, dosing` — S819, S826, S821, S814
Bullet order: dissection as demonstrated warrant (S819) · needling/moxa crossing to Japan (S826) ·
the imported canon renamed into a local school (S821) · chemical pharmacy as a reform programme
(S814). **Guard:** S819 belongs to §3's authority argument but is cited *here* for the technique;
S807 stays theory-only, so S826/S821 carry transmission; no "first anatomist/first pharmacologist"
priority claims.

### §8 `## 8. Crisis: the plague response as public code` — S820, S813, S827
Bullet order: isolation as a legal instrument (S820) · prophylaxis worn as an identifying uniform
(S813) · the case-specific advice text (S827). **Guard:** hygiene infrastructure is bathing §8's;
the prophylactic aromatic object is scent §3–§4's; the boundary logic that makes the sick
polluting is purity §5's. Only the imposed regime, the costume and the advice genre are here.

### §9 `## 9. Boundaries: one-way pointing at the partial owners`
Seven bullets, **zero registry ids**, file+section precision (draft text; integration may polish,
not widen):

- `culture-material/bathing-and-body-hygiene.md` — owns the bath as a water-and-heat institution,
  the five bathing regimes (including the sweat-lodge family) and the purity-vs-hygiene split; its
  §8 already argues bathing as therapy. This entry cites it for regimen bathing and for
  disease-control infrastructure, and never restates its sequences, staffing or fuel logic.
- `culture-material/scent-perfume-aromatics-codes.md` — owns the scent register: manufacture,
  trade, containers, and the prophylactic pomander of its §3–§4. This entry cites it for aromatics
  as a route of administration and for the prophylaxis object, never for perfume chemistry or
  routes.
- `myth-symbol/purity-pollution-boundary-systems.md` — owns the boundary map (its §2) and the
  attribution regimes that decide who is the pollution (its §5). This entry cites that map as a
  constraint on quarantine and cure, and never restates the polarity axes or the carrier ledger.
- `culture-material/funerary-material-culture.md` — owns disposal, assemblage, monument, the
  mourning economy and the death register (its §2–§6). This entry owns the corpse as an object of
  diagnosis and dissection; the disposal law and the death vocabulary are funerary's.
- `myth-symbol/amulets-talismans-apotropaic-marks.md` — owns the amulet's typology, its
  danger-to-remedy table (its §4) and its maker/prescriber classes (its §9). This entry cites it
  for the medical amulet as a *prescription*, not as an object class.
- `myth-symbol/sacred-topography-pilgrimage.md` — owns the shrine, the votive receipt and the
  incubation archive (its §5). This entry cites incubation as a therapeutic technique, not as a
  pilgrimage economy.
- Living-tradition restraint: this entry cites published scholarship *about* traditions and never
  adjudicates a living community's practice or ranks traditions by efficacy; `civilizations/*`
  entries keep their own boundaries and this entry does not restate them.

### §10 `## 10. Lore handoff (one-way; never canon)`
Five bullets, **zero registry ids** (draft text):

- Recipient: lore-shokunin. Canon decisions are theirs; this entry decides nothing about any world.
- Supplied: the code table A–H, the practitioner ladder, the institution checklist, the materia
  classes, the crisis menu, and the medical text genres — as options with the cited anchors
  attached, never as a ranked recommendation.
- Handed over unanswered: which theory frame is orthodoxy and which is heterodoxy; who licenses a
  healer; whether care is temple, state, guild or market; whether the corpse is anatomisable; what
  the plague response is; whether imported technique is marked as foreign.
- Direction: lore may cite this entry; this entry never cites lore, names no canon fact, and makes
  no promotion or clearance verdict.
- Rights caveat: real-world texts and living traditions are cited as published sources; nothing
  here grants a fictional world rights over a living tradition's ritual.

## 4. Bullet template — row `S###` → clause

```
- <clause from that row's BULLET= line> (S<id>)
```

Hard rules for the clause (integration owns the final text; the fragment owns the first draft):

1. One physical line; one id, parenthesised, at the end; no second id and no other parenthesised
   id anywhere on the line. **`BULLET=` lines are inconsistent: some highs already end with
   `(S###)` (S805, S806 at the snapshot below), most do not.** Normalise: strip any trailing
   `\((S\d{3,})\)` from the fragment clause, then append exactly one. Two ids on one line is two
   citations and fails ONEID.
2. Clause text is the fragment's `BULLET=` verbatim (after the id normalisation of rule 1) unless
   it fails rule 3–7; if rewritten, rerun the preflight in §5 before accepting it.
3. 6–25 content words (content word = alphabetic, length ≥ 4, not in accept-c's stopword list).
4. ≥ 3 content words from that row's **first quoted span** of the source cell, in the same
   relative order as in the quote.
5. No verbatim run longer than 12 words from the quote.
6. In-order coverage of the row's `teaches` cell < 80%, and ≥ 1 content word that does not occur
   in `teaches` — i.e. the clause must add the design consequence, not echo the row's own gloss.
7. State fact **and** consequence: what the object/institution/role is, then what it makes a
   culture do (who may treat, who is admitted, what is worn, what is written).
8. No padding openers ("the source says", "according to") — they add no novel content word and
   push the clause toward the teaches echo.
9. The id appears nowhere else in the entry: not in section leads, not in §1, not in §9–§10, not
   in metadata, not in a table.
10. Clause sits in the section assigned in §3; sections list their rows in the order given there.

Shape archetypes from the r66 landed entry (`scent-perfume-aromatics-codes.md`), for rhythm only —
do not reuse their content:
`- <claim with quote words kept in order> - <the design consequence>. (S###)` and
`- <institution/object> <does what> <so a worldbuilder can decide X>. (S###)`

## 5. Assembly and preflight (integration, once fragments exist)

1. Reject a fragment before using it if: `ROW=` does not split into 11 cells by `|`; the id is not
   in S805–S828; tier not A/B; quote span missing, not the first quoted span, or > 25 body words;
   `teaches` under 4 content words or an in-order echo of the quote; live URL not unique against
   `corpus/SOURCES.md` and the sibling fragments; capture target not query-aware equal to the live
   URL. Report defects to the row owner; do not silently repair a source cell.
2. Exact per-row RESTATE preflight (uses the counter's own functions, read-only):

```python
import importlib.util
spec = importlib.util.spec_from_file_location("acc", "reports/round-67/accept-c.py")
acc = importlib.util.module_from_spec(spec); spec.loader.exec_module(acc)
frag = dict(l.split("=", 1) for l in open(
    ".ufo/waves/round-67/rows/ScoutRow01/row-S805.txt").read().splitlines() if "=" in l)
cell = acc.cells(frag["ROW"]); quote = acc.anchor_quote(cell[5])
teaches, clause = cell[6], frag["BULLET"].replace("(S805)", "")
tw, bw, qw = (acc.content_words(x) for x in (teaches, clause, quote))
print(len(acc.content_words(clause)), acc.ordered_hits(qw, bw),
      round(acc.in_order_coverage(tw, bw), 2),
      [w for w in bw if w not in tw])
```

   Accept only `>=6`, `>=3`, `<0.80`, non-empty novel list.
3. After assembly, count ids once: `grep -oE '\(S[0-9]{3,}\)' <entry> | sort | uniq -c` must show
   exactly 24 lines, each `1`, covering S805–S828, and nothing else.
4. Structural check before the counter: 1 H1, 0 H3, ≤ 16 H2, ≤ 250 lines, one `- topic:` line,
   zero ids outside bullets.
5. Run the frozen predicate only inside a materialized clone at the lands commit:
   `python3 -B reports/round-67/accept-c.py --root <clone> --lands <lands>`. A worktree run, a run
   at a moved tip, or a partial-leg paste is not evidence.

## 6. Overlap and collision register (the duplicate-risk set)

| row | collides with | resolution fixed by this plan |
|---|---|---|
| S807 (TCM theory) | S826 (needling transmission) | S807 theory-only in §2; S826 technique+transmission in §7 |
| S805 (humoral) | S812 (Galenic system) | S805 aetiology in §2; S812 system/authority in §3 |
| S808 (Canon) | S821 (Kampo) | S808 the book's travel in §3; S821 local adaptation in §7 |
| S806 (Ayurveda) | S816 (Four Tantras) | separate frames, separate bullets, no blending |
| S818 (apothecary guild) | S823 (barber-surgeons) | two distinct guilds; no "the medical guild" summary |
| S817 (lodge/sweat therapy) | bathing §8 therapy doctrine | therapy institution here; bathing regime there |
| S813 (plague costume) | scent §3–§4 pomander prophylaxis | costume as public office here; aromatic object there |
| S828 (medical amulets) | amulets §4/§9 | prescription here; object and mechanism there |
| S825 (asklepieion) | sacred-topography §5 | incubation procedure here; votive economy/archive there |
| S820 (lazaretto) | bathing §8 infrastructure; purity §5 | imposed legal isolation here; water/heat and boundary map there |
| S824 (sangoma/nganga) | civilizations/* living traditions | published scholarship only; no adjudication, no efficacy claim |
| S827 (consilia) | S808 canon | advice genre (case-specific regimen) vs canon (curriculum) |

## 7. Fragment snapshot — 2026-10-24T12:43:19Z (live wave; re-run before assembly)

24 `row-S*.txt` files existed, **20 of the 24 target rows** (S805, S806, S809–S820, S823–S826,
S821, S822); **4 target rows absent**: S807, S808, S827, S828. Four files carried ids outside the
claim set (S829–S832). Measured with accept-c's own `cells`/`anchor_quote`/`content_words`/
`ordered_hits`/`in_order_coverage` (read-only, no counter run):

| finding | ids | effect if landed unchanged |
|---|---|---|
| id outside S805–S828 (all four tier C, status `rejected`, used-by `—`; anchor quote unusable — S830 3 words, S831 2 words, S829/S832 none; capture absent except S830) | **S829, S830, S831, S832** | **Sequencing constraint (L1 ruling):** these are legal only at Ca's lands commit **A_ca**, after claim C's receipt has been taken at its own lands **A_c** where the tree carries only S805–S828 over base (plus S801–S804 landed earlier at A_r). If any of S829–S832 is present when `accept-c.py` runs at A_c, APPEND reports it as `extra=<id>` → FAIL. Never commit them before A_c's receipt exists. |
| `< 3` in-order quote words in the fragment clause | **S813 (2), S826 (2)** | RESTATE FAIL (`quote_words`) — clause must be rewritten by the row owner, keeping quote words in order |
| `teaches` echoes the anchor quote (in-order coverage 1.00 ≥ 0.80) | **S824** | RESTATE FAIL (`teaches_echoes_quote`) — a row-cell defect no bullet rewrite can fix; the teaches cell must add analysis, not repeat the gloss |
| novelty floor only just met (1 novel content word) | **S811** | passes today, but fragile: the entry clause must keep at least one word absent from `teaches` |
| `BULLET=` already ends with the id | **S805, S806** | normalise per §4 rule 1 or the line carries two citations (ONEID FAIL) |
| fragment churn observed inside the wave | S806 hits 2 → 7, S817 2 → 3, S818 2 → 3, S821/S822 landed late and pass, between 12:39Z and 12:43Z | any audit is a snapshot; re-measure after the last row lands |

All other present fragments passed the arithmetic legs (11 cells, tier A/B, status mined, opened
2026-10-24, used-by the entry, live URL + same-page capture) at the snapshot.

## 8. Open dependencies (recorded, not assumed)

- 4 target rows and their `BULLET=` clauses are still absent (list above); the entry cannot be
  assembled until they land. Fragments already on disk are being rewritten live — treat every
  metric as a snapshot and re-run §5's preflight after the last row lands.
- The README row and the metadata `- verified-at:` text are other seats' artifacts; the entry's
  `- topic:` must be copied verbatim into that row (TOPIC leg) or the claim fails.
- No leg of this plan may be reported as executed: the preflight and the counter run at lands.

