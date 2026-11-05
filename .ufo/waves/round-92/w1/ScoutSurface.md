# ScoutSurface — round 92, claim C surface map

Seat: ScoutSurface · Lane: kotodama · Wave r92/w1 · Date: 2026-11-05
Base: `21350361500aa000b90f91082bf9d7295a9c24cd` · Freeze: `066b9728fc64e78735769c4740d05c1000d31a3b`
Stage file: `.ufo/waves/round-92/w1/stage/ScoutSurface/surface-map.md` (full commands + outputs)

## Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/stage/ScoutSurface/surface-map.md` — the surface map, every command and its output
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/ScoutSurface.md` — this report

No other file was written or modified. No git/jj mutation of any kind.

## Numbers measured (base; corpus/ is byte-identical base↔freeze)

| measure | command | value |
|---|---|---|
| filename owners in `corpus/knowledge` | `git ls-tree -r --name-only <base> corpus/knowledge \| grep -icE '(ideophone\|mimetic\|onomatopoe)'` | **0** (grep rc=1) |
| same over whole `corpus/` | same, `corpus` | **0** |
| same at freeze | same, `<freeze>` | **0** |
| linguistics partition files | `git ls-tree -r --name-only <base> corpus/knowledge/linguistics \| wc -l` | **36** (freeze: 36) |
| entry path at base | `git show <base>:corpus/knowledge/linguistics/ideophones-mimetics.md` | **rc=128**, does not exist |
| entry path at freeze | `git show <freeze>:…/ideophones-mimetics.md` | **rc=128**, does not exist |
| README `## linguistics/` header | `git show <base>:corpus/README.md` line 344 | `## linguistics/ (36)` |
| README linguistics rows | index-tool parser over materialized base tree | declared **36**, files **36**, rows **36** (34 in-section + 2 supplemental owned by linguistics) |
| README lists an ideophone entry | `grep -c 'ideophones-mimetics' corpus/README.md` | **0** — absent |
| README live totals + footer | lines 974/976/978 | `Total knowledge entries: 263.`; `Counts checked 2026-11-05`; `(total 263 files; directory totals 36/36/43/29/24/95)` |
| index tool on base tree | `python3 -B tools/check-corpus-index.py --root <base-tree>` | `CORPUS-INDEX: OK files=263 rows=263 findings=0`, **rc=0** |
| registry | `git show <base>:corpus/SOURCES.md` | **880** rows, last id **S956** |

## Nearest owners — where ideophone-adjacent material lives

**`corpus/knowledge/linguistics/sound-symbolism.md`** (155 lines, 28980 bytes) — the
substantive owner. Ideophone material at lines **1** (H1 `— Iconicity, Ideophones, and
the Sound–Meaning Interface`), **3** (`- topic:` already advertises "an ideophone-register
design procedure"), **11** (Dingemanse 2012/2015/2018), **15** (Hamano 1998, Kita 1997),
**18** (recheck: "before citing ideophone morphosyntax"), **23** (gap statement),
**27** ("imitative: onomatopoeia proper"), **38** (table row "mimetic/ideophone
stratum"), **99** (`## 6. Ideophones — the depictive class (the biggest lever for a
mimetic-rich culture)`), **101–111** (class definition, inverse expressiveness↔
integration grammar profile, reduplication, Japanese giongo/gitaigo, the 5-step
ideophone register design procedure, diachrony), **143/146–148** (decision record,
D7 calls the ideophone procedure "the usability deliverable"), **153**.

**`corpus/knowledge/linguistics/register-lexicon-ceilings.md`** (317 lines, 36139 bytes)
— mention-only: **lines 303, 306, 315**, all inside `## 12. Errata (round 33)`, and all
back-references *to* `sound-symbolism.md` correcting a false absence sweep (`X63-F2`).

**Correction to claims.json `C.surface`:** it says `register-lexicon-ceilings.md` carries
a "mimetic mention". It does not — `grep -n -i 'mimetic'` on that file returns **0**
(rc=1). Its two hits are the word "ideophone" (lines 306, 315). The claim's conclusion
is unchanged (no dedicated entry owner), but an entry "gap filled" line asserting the
mimetic mention would be false on the committed bytes.

**Two owners claims.json `C.surface` does not name:**
- `corpus/knowledge/synthesis/myth-to-language-derivation.md:32` — the corpus's existing
  classification table row for ideophones (synthesis partition, not linguistics).
- `corpus/knowledge/linguistics/register-strata-attestation.md:69` and
  `semantics-pragmatics.md:95` — the Searle speech-act class "expressives", a different
  sense from ideophone expressiveness; the new entry's `expressive` anchor must
  disambiguate.
- `corpus/knowledge/myth-symbol/ritual-liminality.md:130` — "mimetic" = Girard's mimetic
  theory, a third unrelated sense.

## Six topic phrases in the base corpus

`git grep -l -i` per phrase at base:

- `ideophone` → sound-symbolism.md, register-lexicon-ceilings.md, synthesis/myth-to-language-derivation.md
- `mimetic` → sound-symbolism.md, myth-symbol/ritual-liminality.md, corpus/SOURCES.md
- `onomatopoeia` → sound-symbolism.md, culture-material/music-instrument-lexicon.md
- `depictive` → sound-symbolism.md, synthesis/myth-to-language-derivation.md
- `expressive` → 12 files (3 civilizations, 2 culture-material, 3 linguistics, myth-symbol, 2 synthesis, SOURCES.md, lessons/round-5.md, lessons/round-5-sources/13.json)
- `sound-symbolic` → sound-symbolism.md, synthesis/myth-to-language-derivation.md

Word-bounded occurrences over `corpus/knowledge`: ideophone 26/3 files, mimetic 11/2,
onomatopoeia 2/2, depictive 5/2, expressive 15/11, sound-symbolic 6/2.

**Dedicated-entry owner check → none.** Three independent negative tests:
filename owners 0; exactly one matching H1 in all of `corpus/knowledge`
(`sound-symbolism.md`, whose owning topic is sound symbolism/iconicity, not the ideophone
word class); exactly one matching H2/H3 in the partition (`sound-symbolism.md:99`), a
section inside a differently-owned file. `corpus/README.md` mentions any of the six
phrases on exactly one line (372, the `sound-symbolism.md` row).

## Boundary the entry must name honestly

The sharpest risk is not absence, it is **overlap**: `sound-symbolism.md` §6 already
holds a full "Ideophones — the depictive class" section with a class definition, a
grammar profile, the Japanese mimetics system, and a 5-step ideophone-register design
procedure, and its §9 D7 already names that procedure its "usability deliverable". The
new entry can own the typological word-class framing, the Cushitic/Ethiosemitic grammar
(S958 Kambaata, S959 Amharic), the sensory semantics, the acquisition/processing
material, and a fuller design procedure; it **cannot** present the ideophone design
procedure, the Dingemanse typology, or the Hamano/Kita Japanese system as new. This is
consistent with claims.json `C.bounds` ("does not absorb … the sound-symbolism material
already held in sound-symbolism.md"), but the entry's own gap/boundary text must be
drawn at the section level, not the file level.

**Grader note** (freeze-pinned `tools/check-advance-evidence.py:482–498`): the six phrases
are counted **only in the new entry's own h2 headings and table cells**, with
`span = len(hit_heads) + (1 if hit_rows else 0)`. `min_topic_phrases=4` and
`min_anchor_span=3` therefore require ≥4 of the 6 phrases present in the entry's
headings/table, spread over ≥3 heading/table surfaces. The base-corpus counts above are
surface-map facts, not grader inputs.

**README landing arithmetic** (index tool compares row topic to the entry's `- topic:`
verbatim): `## linguistics/ (36)` → **37**; `Total knowledge entries: 263.` → **264**;
footer total 263 → **264**; footer directory totals `36/36/43/29/24/95` →
`37/36/43/29/24/95`; plus one new row `- \`ideophones-mimetics.md\` — <topic>` with the
entry's topic text verbatim. All four numbers must move together or the tool raises
`HEADER_DRIFT` / `TOTALS_DRIFT` / `FOOTER_TOTAL` / `FOOTER_DIR_TOTALS`.

## Commands run (rc)

```
git log -1 --format='%H %ad %s' --date=iso 21350361500aa000b90f91082bf9d7295a9c24cd      rc=0
git log -1 --format='%H %ad %s' --date=iso 066b9728fc64e78735769c4740d05c1000d31a3b      rc=0
git diff --stat <base> <freeze> -- corpus/                                               rc=0 (no output)
git ls-tree -r --name-only <rev> corpus/knowledge | grep -icE '(ideophone|mimetic|onomatopoe)'   rc=1, count 0
git ls-tree -r --name-only <rev> corpus           | grep -icE '(ideophone|mimetic|onomatopoe)'   rc=1, count 0
git ls-tree -r --name-only <rev> corpus/knowledge/linguistics | wc -l                    rc=0, 36
git show <rev>:corpus/knowledge/linguistics/ideophones-mimetics.md                       rc=128 (both revs)
git show <rev>:corpus/README.md                                                          rc=0
git show <base>:corpus/SOURCES.md | grep -c -E '^ {0,3}\| *S[0-9]+'                      rc=0, 880
git show <base>:corpus/SOURCES.md | grep -o -E 'S[0-9]{3,}' | sort -u | tail -3           rc=0, S954/S955/S956
git grep -l -i -E '<phrase>' <base> -- corpus/knowledge corpus/lessons corpus/SOURCES.md  rc=0 (x6)
git archive <base> | tar -x -C <scratch>/base-tree                                      rc=0
grep -rIioE "\b<phrase>" corpus/knowledge/ | wc -l  (x6)                                  rc=0
grep -rn -i -E '^#{2,3} .*(ideophone|mimetic|onomatopoeia|depictive|expressive|sound-symbol)' corpus/knowledge/   rc=0, 1 hit
python3 -B tools/check-corpus-index.py --root <scratch>/base-tree                         rc=0, CORPUS-INDEX: OK files=263 rows=263 findings=0
```

## Could not measure

- The lands surface (post-landing state) does not exist; no lands-side numbers claimed.
- `corpus/lessons/round-92.md` exists at neither base nor freeze, so no gate-line
  measurement was possible.
- Whether the two supplemental `conlang-scholarship*` rows stay supplemental at lands is
  an L1 integration choice; either form passes the index tool, but the linguistics row
  count must land at 37.

## Tooling

None installed or upgraded. Work used `git` (read-only: log/ls-tree/show/diff/archive)
and the lane's own `python3` + `tools/check-corpus-index.py`. No pacman transaction, no
sysctl, no PATH-directory writes, no network fetch (the S957–S960 captures were already
committed at the freeze and were only read). Scratch `/fast/scratch/hyaku/kotodama-r92/ScoutSurface/`
was deleted before this report was written.
