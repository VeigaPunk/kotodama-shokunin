# ScoutSurface97 — Report (claim C coverage surface + adjacency, 2026-11-05)

Full findings: `.ufo/waves/round-97/w1/stage/ScoutSurface97/surface.md` (sha256 43ad0a2eed43f6d937a2a5f47825d580ee0a2cbbc8df66904018d74f82db4b2e). Read-only seat: no lane file outside the stage touched, nothing committed, no tools installed.

## Numbers (command + rc on every one)

- Frozen sweep: `python3 -B reports/round-97/sweep-control.py --root <lane>` → rc 0, `R97-BASE base=1ffc5a83… files=268 owners=0 []`, `SWEEP-CONTROL: PASS` (R96-REPLAY owners=2: binding-speech-complex.md, sacred-kingship-mythic-charter.md). Paste in surface.md §1.
- Body sweep (16-term pattern, verbatim seat command) → rc 0, 59 matches / 32 files; token histogram rc 0 (satire 24, nith 14, senna 9, boast 7, invective 3, flyting 3, Hija 3, …). Full per-line table with class in surface.md §3.
- Owner check: same grep piped to count content starting `#` → 0 (rc 0); `- topic` → 0 (rc 0). All 59 hits are prose/list/table cells: **0 topic-line or heading owner of any frozen phrase — C8 zero-owner premise holds by content.**
- Frozen-phrase base status: verbal duel 0, ritual insult 0, song duel 0, boast formula 0, audience adjudication 0, flyting 3 (orality-formulaic-language.md:112; trickster.md:25, :62) — matches claims.json before-state.
- Entry absent: `test -e corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` → rc 1.
- Partition counts (`find | awk | sort | uniq -c`, rc 0): civilizations 95, culture-material 43, linguistics 41, myth-symbol 36, synthesis 29, verification 24; 268 total. linguistics/ justified in surface.md §6.

## Classification (surface.md §3)

0 owners; 22 substantive sections (orality :112 flyting+senna licensing item, :60 izibongo; trickster :35 senna genre slot, :62 flyting clown, :69 the dozens; arabia :69 Fakhr / :71 Hijāʾ table rows; oath entry :84/:120 S979 satire requirements; yoruba :123/:130/:136 Gelede; masks :41 one-owner row, :80 kolam lampoon; celts :50/:74/:76/:179 bardic praise-satire; creation-myths :49 boasting taboo; pastoralism :152 taunt cell); 30 passing; 7 false-positive tokens (nith⊂zenith/senith, Senna⊂Sennacherib, Hija⊂Hijazi/Hijaz/hijab, Satire=Persius).

## Adjacency boundaries (surface.md §4 — defer, do not restate)

orality-formulaic-language.md owns meter/epithet/licensing machinery (flyting+senna are two words in its :112 checklist); trickster.md owns the figure and the dozens' signifying pragmatics (Gates 1988); arabia-pre-islamic.md owns the qaṣīdah mode table (Fakhr/Hijāʾ rows); binding-speech-complex.md owns binding/enforcement (níð, self-imprecation topic line); oath-blessing-curse-formulae.md owns formula slot grammar and satire-as-curse (S979); politeness-taboo-euphemism.md owns enregisterment metadiscourse; yoruba.md + masks-masquerade.md own the Gelede performance account (one-owner row already declared); celts.md owns bardic institutions. New entry: contest genres, rules, adjudication, design procedure; cite neighbours by path; follow the one-owner-boundary table convention.

## Skeleton (surface.md §5)

10 h2 (6 required): 1 verbal duel · 2 flyting+senna · 3 ritual insult · 4 song duels · 5 boast formula · 6 audience adjudication · 7 rules that keep insult ritual · 8 one-owner boundary table · 9 design procedure + micro-example · 10 calibration. All six frozen phrases placed (5 in h2, headroom in the 7-row × 4-col taxonomy table). Registry: S985+ rows continuing S980–S984 shape (highest S984 at SOURCES.md:941, all mined 2026-11-05, used-by oath entry), `used-by` exactly the new entry path, captures under reports/round-97/evidence/.

Blockers: none. Scratch /fast/scratch/hyaku/kotodama-r97/ScoutSurface97/ removed before yield.
