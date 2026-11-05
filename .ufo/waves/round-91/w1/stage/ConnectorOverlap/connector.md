# ConnectorOverlap — sibling-overlap scan, round-91 C entry (planned)

Seat: ConnectorOverlap (leaf, read-only). Lane HEAD/freeze `691aebf2`, base `d39434b3`, 2026-11-05.
Scope rule honored: overlap and open cells only; no prescription of entry content.

## State observation (material)

`git status --porcelain` shows `?? corpus/knowledge/linguistics/secret-and-ludic-languages.md` — an
untracked working-tree draft (21,472 bytes; `ls corpus/knowledge/linguistics | wc -l` → 36 vs
`git ls-files -- corpus/knowledge/linguistics | wc -l` → 35). At git level the brief's "planned, not
yet written" is accurate: `git ls-files --error-unmatch <entry>` rc=1. The sibling table below
covers the 35 committed entries only; the untracked draft is excluded from it (it is the planned
entry, and it already names the two adjacent owners in its §1).

## Overlap table

| sub-topic | verdict | path:line evidence | command |
|---|---|---|---|
| argot and cant as closed in-group vocabularies | held | `corpus/knowledge/linguistics/linguistic-anthropology.md:115` (§5.3 "Thieves' argot and anti-languages", dedicated section), `:117-123` (Halliday mechanisms; resocialization; turnover), `:125` (Harman 1566 → Polari corpus list); `corpus/knowledge/linguistics/sociolinguistics-registers.md:84` (anti-language paragraph; Elizabethan canting, grypsera, Polari Baker 2002); `corpus/knowledge/synthesis/religion-language-co-evolution.md:15,:88-90` (priestly cant as bounded specialist repertoire); `corpus/knowledge/culture-material/trade-economy-lexicon.md:103` (trade tongues and cants; Harman; Cockney rhyming slang) | `grep -ni argot corpus/knowledge/**`; `grep -niE '\bcant\b' corpus/knowledge/**` |
| anti-languages (Halliday) as social structure maintained through conversation | held (concept); sub-cell "maintenance through conversation" unowned | `linguistic-anthropology.md:115-123` (§5.3 dedicated); `corpus/knowledge/linguistics/dialect-register-consistency.md:71-77` (§5 anti-language formation, dedicated section), `:91` (§6 row 7), `:116` (DR-DC-06); `sociolinguistics-registers.md:84`; `corpus/knowledge/linguistics/register-lexicon-ceilings.md:182` (operation row); closest to the conversational-maintenance angle: `corpus/knowledge/synthesis/dialect-faction-map-workflow.md:121-123` (motives incl. concealment/solidarity; threat model) — no sibling states a conversation-maintenance test | `grep -niE 'anti-language\|antilanguage\|halliday' corpus/knowledge/**` |
| backslang and reversal games | partial | backslang only passing: `linguistic-anthropology.md:121` (deformation mechanism list); reversal operations owned as ceiling material: `register-lexicon-ceilings.md:180,:183` (verlan row, Gotowski 2019; language-games row), `corpus/knowledge/linguistics/register-strata-attestation.md:390-402` (reversal-ceiling mechanism), `register-lexicon-ceilings.md:13` (Gotowski source block); no sibling owns backslang itself as a register/game | `grep -niE 'backslang\|back-slang\|reversal' corpus/knowledge/**`; `grep -ni verlan corpus/knowledge/**` |
| ludling and Pig Latin style word play | partial | `linguistic-anthropology.md:136` (§5.4 decision-table row "Ludling (word game) ... Verlan, Pig Latin"), `:146` (checklist "ludlings for children"); `register-lexicon-ceilings.md:183` (language-games row; Tagalog tadbaliks/baliktád); no dedicated ludling section anywhere | `grep -niE 'pig latin\|ludling\|ludic' corpus/knowledge/**` |
| in-group concealment and identity functions | partial | `dialect-faction-map-workflow.md:121-123` (separate motives incl. concealment and solidarity; secrecy threat model), `:202` (anti-society as analytical interpretation); `corpus/knowledge/linguistics/sociolinguistics-registers.md:126` (era row "no in-group code for networked youth"), `:86` (uchi/soto in-group footing, honorifics); `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:26,:42` (secrecy-by-channel vs secrecy-by-vocabulary boundary, routes anti-languages to `sociolinguistics-registers.md:84`); `corpus/knowledge/civilizations/australia-aboriginal.md:66` (avoidance vocabularies "not one 'secret language'"); no dedicated section | `grep -niE 'in-group\|ingroup\|covert\|secret language\|secret register\|conceal' corpus/knowledge/**` |
| design procedure for a fictional secret register | partial (distributed) | `linguistic-anthropology.md:139-149` (§6 checklist, `:146` special-language step); `sociolinguistics-registers.md:135-136` (§9 communities-of-practice checklist; overlexicalization zones); `register-lexicon-ceilings.md:3` + §3 (measurement procedure, but only for operation-built registers); `dialect-faction-map-workflow.md:123` (threat-model step); no single entry owns a unified secret-register design procedure | same greps (distributed synthesis) |

## PROVINCE.md verdict

PROVINCE.md has no Core/Frontier/Adjacent headings; its sections are **Domain / Owns / Refuses /
Adjacent contract** (read in full, 2026-11-05). The planned entry falls in **Owns**: the linguistics
partition is listed verbatim (`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`).
No sibling owner is named in PROVINCE.md for this entry. Named boundary parties: lore-shokunin
(canon/world bible, Adjacent contract + Refuses), chousa (general source-research method, Refuses),
kotoba and kake (Refuses). Inside the corpus, the frozen claim C names the adjacent owners:
`linguistics/linguistic-anthropology.md` §5.3 and `synthesis/religion-language-co-evolution.md` §6
— exactly the two `held`/anchor files the table shows.

## considerthese

Expected absent; confirmed absent:

```
$ ls -la /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese
ls: cannot access '/home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese': No such file or directory
rc=2
```

Consistent with frozen `claims.json` → `assimilation`: "kotodama has no considerthese directory."

## Open cells (overlap summary, no content prescription)

1. argot/cant — closed by §5.3 (held); religion-language-co-evolution §6 closes the sacred-cant variant.
2. anti-language concept — closed (§5.3 + dialect-register-consistency §5); the conversational-maintenance
   design test is unowned.
3. backslang as such — open at entry level (passing mentions only); reversal-operation mechanics held by
   register-lexicon-ceilings.md (ceiling angle).
4. ludling/Pig Latin — open at entry level (table row + passing mentions only).
5. in-group concealment/identity — open at entry level (motive lists and a channel-vs-vocabulary
   boundary row only).
6. unified secret-register design procedure — open (distributed fragments across four entries).

## Risks (second-order, stated not scored)

- Collision risk sits exactly where frozen claim C already puts it: any restatement of §5.3's mechanism
  list or the §5.4 catalogue duplicates the named adjacent owner; the C claim's bounds line explicitly
  does not absorb that material.
- Reversal content must not silently absorb register-lexicon-ceilings.md's ceiling procedure (it owns
  operation-domain measurement); overlap there is the largest re-statement hazard after §5.3.
- The untracked draft on disk will change `ls corpus/knowledge/linguistics | wc -l` from the frozen 35
  to 36 once integrated; the frozen surface check correctly reads git, not the working tree.
