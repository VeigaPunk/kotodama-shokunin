# ScribeEntry98 — Report (kotodama round 98, w1, claim C entry writer)

Seat: ScribeEntry98 (leaf member; writes only the entry, the corpus index row, this report and the
stage files). Round: kotodama round 98, attempt 1. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

## 1. Files written (nothing else was touched)

| path | what | bytes |
|---|---|---|
| `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` | the new knowledge entry (only writer) | 47370 |
| `corpus/README.md` | index row + `## linguistics/ (42)` → `(43)` + new `## Round 98 toast and drinking-speech entry` section | +22/−1 lines |
| `.ufo/waves/round-98/w1/stage/ScribeEntry98/self-check.txt` | the self-check receipt | ~4.6 kB |
| `.ufo/waves/round-98/w1/stage/ScribeEntry98/mkselfcheck.py` | the script that produced it | — |
| `.ufo/waves/round-98/w1/ScribeEntry98/DONE` | sha256 of the entry (written last) | — |

No frozen file (`claims.json`, `predispatch.py`, `predispatch-base.txt`, `controls/**`), no round-97
file, no `corpus/SOURCES.md` row, no `reports/round-98/evidence/**` file and no other lane was
edited. Nothing was committed, staged or pushed (read-only git only: `git status --porcelain`,
`git diff --stat corpus/README.md`).

Scratch `/fast/scratch/hyaku/kotodama-r98/ScribeEntry98/` was used and deleted before this report.

## 2. Dependencies (bounded wait)

Waited with `for i in $(seq 1 180); do [ -f <dep> ] && break; sleep 60; done` for
`stage/ScoutSurface98/DONE`, `stage/ConnectorOverlap98/DONE`, `stage/ExecRegistry98/DONE`.
All three appeared; `ScoutSurface98/surface.md`, `ConnectorOverlap98/overlap.md` and
`ExecRegistry98/rows.md` were read before drafting. `reports/round-98/evidence/manifest.json` and
the 11 capture files were read before any citation was written.

## 3. The entry (claim C surface)

- **Topic line**: byte-equal to the frozen topic (em dash U+2014, ASCII apostrophe in
  `toastmaster's`). `self-check.txt` → `topic line byte-equal to frozen topic -> PASS`.
- **Size**: `bytes=47370 (floor 12000) -> PASS`.
- **Structure**: `h2=13 (floor 6) -> PASS`; the rite table is `7 data rows x 5 cols
  (floor 5x3) -> PASS` (§8 "The stages of a toast sequence": stage / office and who speaks /
  what the stage carries / cup action / refusal and exit option).
- **Frozen phrases**: `6/6` present in h2 headings or table data rows (floor 4) —
  *toast formula* (§2 h2), *health-drinking* (§3 h2), *libation* (§4 h2), *toastmaster* and
  *toast sequence* (§5 h2), *drinking oath* (§6 h2). All six are h2 headings, so the count does
  not depend on table cells.
- **Content**: reference and generative method only. Canon is deferred to lore-shokunin
  ("Canon and rights are outside the door", "The package lore-shokunin receives"), research
  method to chousa. Boundaries from `overlap.md` §3 are honoured by deferral, never by restating:
  vessel names → `vessel-container-lexicon.md`; the feast/meal → `cuisine-food-lexicon.md`;
  bond, breach ladder and penalty law → `guest-right-hospitality-law.md`; binding-slot grammar →
  `oath-blessing-curse-formulae.md`; boast/taunt/riposte grammar → `verbal-duelling-ritual-insult.md`;
  vow mechanics → `petitionary-and-votive-formulae.md`; the room → `furniture-interior-lexicon.md`;
  libation to the dead → `death-afterlife-eschatology.md`. No vessel name, vessel-naming rule,
  boast slot, sanction grammar or hospitality-law provision is restated.
- **Required apparatus**: a decision procedure (§9, three phases plus a NON-CANON worked
  micro-example), the four named error patterns — toast with no addressee, cup with no order,
  oath-cup confused with the toast, refusal with no cost (§10.1–§10.4, plus eight more) — and a
  checklist (§11).
- **Prose independence**: shared 8-grams vs `verbal-duelling-ritual-insult.md` = **11**, vs
  `oath-blessing-curse-formulae.md` = **6**, vs `guest-right-hospitality-law.md` = **0**
  (round-97's first draft had 294 against its neighbour; the landed round-97 entry has 35). The
  residual shared spans are header/boilerplate lines (the `couples:` line, `verified-at:`), not
  prose.
- **Cited-line discipline**: `MULTI-ID lines=0 TABLE-ID lines=0`; every cited line carries
  exactly one S-id and no table row carries an id, so the entry passes QUALITY criterion 15.

## 4. Cited ids and where each supports a claim

Cited ids (each appears in the entry text at the claim it supports, and again in the §8 grounding
list): **S994, S995, S996, S997, S998, S999, S1000, S1001, S1002, S1003, S1004** — 11 ids, i.e.
every qualifying row opened this round for this entry. `qualifying uncited: []` and
`entry cites ids absent from the registry: []` in `self-check.txt`.

| id | source | the claim it supports in this entry |
|---|---|---|
| S994 | Laing 1844, *Heimskringla* (brage-goblet) | §5 the cup-order of the Norse feast (victory → peace → oath-cup → remembrance goblet); §6 the vow-cup note and the memory-turn goblet |
| S995 | *Heimskringla*, Ynglinga saga ch. 36 | §6 the recorded drinking oath: stand to the *bragafull*, swear, drink, then take the seat |
| S996 | Plato, *Symposium*, tr. Jowett | §4 libations and the hymn before drinking; §7 consent-based drinking, no compulsion |
| S997 | Xenophon, *Symposium*, tr. Dakyns | §6 the pledge exchange in the round and the cup-bearers' regulated circuit |
| S998 | Athenaeus, *Deipnosophists* vol. 3, tr. Yonge | §4 the pledge-cup to the Good Deity, the unmixed-wine sample, the removal of the tables |
| S999 | Tuite 2005, *The Autocrat of the Banquet Table* | §5 the toastmaster's office (*tamada*), the themed round, the rigid opening order, the single-draught rule |
| S1000 | *Beowulf*, tr. Gummere | §5 the cup distributed by rank, and the answer when it reaches the guest |
| S1001 | *Open Encyclopedia of Anthropology*, "Feasting" | §2 the toast as one act joining communication and consumption, and its choreography |
| S1002 | Giles 1842, *History of the Kings of Britain* | §2/§3 the health-drinking exchange: the lady's phrase and the prescribed answer (*Drinc heil*) |
| S1003 | Legge 1885, *Li Ki* bk. XLII | §3/§4 the prepared cup, the reciprocal bow, the shared vessel between host and guests |
| S1004 | Duthille, *Drinking and Toasting in Georgian Britain* | §7 the toastmaster's compulsory glass, the principled refusal, refusal as mark of independence |

**Evidence binding (C7 shape, measured on the landed bytes):** for all 11 ids the manifest quote is
1–25 words, occurs exactly **once** in the named `quote_capture`, appears in the registry row's
anchor cell, and every `captures[].sha256` matches the file on disk —
`C7-shaped binding over the 11 qualifying ids -> PASS`. `S1005` is the S992 supersede row and
belongs to the duelling entry; it is not cited here.

**Sentence support (round-97 lesson R97-M3).** Every double-quoted fragment in the entry body was
counted in its capture: `body quoted fragments=5 unmatched in any capture=0`. Three illustrative
strings that were not source quotes were rewritten out of quotation marks before landing
(*all of us to be well*, *everyone in general*, *they drank*, *nothing at all*), so no quotation in
the entry is unattributed.

## 5. Uncited claims — inference list

Seven statements are readings the sources support without stating, and each is marked *inference*
in the body and listed in §13: the toast's distinguishing slots (cup + shared uptake); the order
of a sequence as checkable social ranking; a refusal as four assertions with the opened debt as
the hinge; the reciprocal debt chain as what makes a rite social; the boast-cup and memory-turn as
one machine with two contents (the *reading* is this entry's; the two turns themselves are S994);
a drinking oath without a stated cost being a toast; and the unstated libation direction as the
commonest drafting failure. All design apparatus (slot list, sequence stages, error patterns,
checklist, procedure, worked example) is marked *design, not sourced* / NON-CANON.

## 6. Index (claim C5)

`corpus/README.md`: `## linguistics/ (42)` → `(43)`; the new row inserted in filename order
between `taboo-strata-lifecycle.md` and `toponymy-place-names.md` with the entry's `- topic:`
text verbatim; a new `## Round 98 toast and drinking-speech entry (2026-11-05)` section appended
after the round-97 one, carrying the totals line `Total knowledge entries: 270.` and a footer
block `(total 270 files; directory totals 43/36/43/29/24/95).`

```
$ python3 -B tools/check-corpus-index.py --root .
rc=0 | CORPUS-INDEX: OK files=270 rows=270 findings=0
```

Also run, both rc 0: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--file corpus/SOURCES.md` (`file ok …/corpus/SOURCES.md`) and `python3 -B tools/check-cited-lines.py
corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` (`CITED-LINES: 0 finding(s) in
1 file(s)`). Full receipts: `stage/ScribeEntry98/self-check.txt`.

## 7. Content sweep (C8)

Re-run over the landed tree with the counter's own rule (topic line or any markdown heading
carrying a frozen phrase, entry excluded): `files scanned=270 other owners=0 [] -> PASS`. No other
knowledge file's topic line or heading was given a frozen phrase; no other knowledge file was
edited.

## 8. Known limits and out-of-scope items

- The entry's claims about the Georgian supra (S999) and the eighteenth-century British toast
  (S1004) are bounded to those texts and are not generalised; the registry rows carry the same
  bound.
- The legend behind *Drinc heil* (S1002) is a literary episode, and the entry says so; it is not
  offered as a history of toasts.
- S994's "cup over which vows were made" is the edition's endnote, and the entry attributes it to
  the edition rather than to the saga.
- The counter's C9 leg (non-author re-open by ReviewerC98) is not mine: it depends on
  `.ufo/waves/round-98/w1/stage/ReviewerC98/reopen.json`, which ReviewerC98 writes.
- The registry rows S994–S1004 and the evidence manifest are ExecRegistry98's; this seat only
  cites them.
- The lowest-axis obligation is not met or waived by this seat (freshness stays paused under the
  open L0 questions; the round's claims move no freshness observable).

## 9. Tooling

None installed or upgraded. No pacman, no uv/cargo/npm install, no host sysctl touched, no
network fetch by this seat (every source was opened by ScoutSources98 and re-opened by
ExecRegistry98; this seat read the committed captures only).

## 10. Acceptance

- Entry exists at `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md`, sha256
  `0724a044fa33a50bf69c021600561b7e40e067b9cf8bf09bcd774cfa16d9d4cf`.
- `corpus/README.md` edited; index checker rc 0.
- `stage/ScribeEntry98/self-check.txt` written with every number and its command and rc.
- `stage/ScribeEntry98/DONE` written last, containing the sha256 above.
- Nothing committed by this seat.
