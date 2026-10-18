# Round 29 adjacency audit — province entries

Scope: claim A in `reports/round-29/claims.json:25-30`, limited to the two round-28 knowledge entries, `PROVINCE.md`, and the world-bible integration contract. This is a scope/provenance review, not a canon, legal-rights, or cultural-permission ruling.

## Verdict

**PASS on province boundaries; evidence defect recorded.** The reviewed entries are linguistic-cultural method/reference material, label the D4 exercise as NON-CANON, and reserve canon decisions to lore-shokunin. Their use of speech-act and institutional vocabulary is analytical and applied to an invented design exercise; it does not rule on real-world rights, certify permission, or add game mechanics. No Province or contract change is indicated.

The source sweep found one authoring defect and three sibling landings. These are evidence/reporting findings, not out-of-province content. They are recorded here without editing either corpus entry, consistent with this assignment's report-only write scope.

## Province and contract boundary

`PROVINCE.md:1-14` assigns this lane linguistic-cultural worldbuilding and its own corpus, gates, examples, and reports; it explicitly says these partitions do not extend ownership to general research methodology, historical truth certification, or lore's canon. `PROVINCE.md:16-25` reserves canon to lore, refuses real-world rights/attribution rulings, names lore as world-bible owner, and directs contested scope to the integrator. `AGENTS.md:3-13` likewise restricts work to this repo and says canon decisions belong to lore.

At 2026-10-18T21:02:17Z, `sha256sum PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` returned respectively `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`, `be3a9477ed28ba401352ebce7c182d529223e552d0dba0d75f3b97b956be2c8b`, and `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`. At that same time, `git diff --name-status 3b13a2f2821ed6f8ac1217842ab6830d592c7935 -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` returned no paths; lane HEAD was `e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`. The Province, local instructions, and contract therefore remain unchanged from the declared round-29 baseline in this check.

The contract is load-bearing but not activated by these entries. Its §§1 and 6 distinguish method/reference from a world-bible assertion, require bilateral same-revision read records, and leave that acknowledgement **pending** until both records exist. §§4 and 8 define a packet, submission, receipt, disposition, and canonized import as separate steps; §10 routes rights/restricted-knowledge questions to the operator or authorized specialist; §11 says citation or access is not permission. The two corpus entries are not handoff packets and do not claim receipt, acceptance, or canonization. The contract itself and the round-28 packet record at `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14` both preserve the pending acknowledgement; this audit does not infer a lore-side acknowledgement or rights clearance.

## Deliverables reviewed

- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:1-3,241-248` describes a measurement/design method, labels the D4 stamp register NON-CANON, and sends canon decisions to lore. Its real-world examples are linguistic analogues, not statements about any real community's legal rights or permissions.
- `corpus/knowledge/linguistics/register-strata-attestation.md:1-3,34-45,47-72,90-103,298-313` separates the speech variety from the hypothetical law over it, presents Austin/Searle as a designer's toolkit, marks the D4 drill NON-CANON, and reserves fictional truth and canon to lore. The phrase “rights, duties, permissions” at `:17` is the stated theoretical vocabulary for Searle's deontic powers, not a ruling about anyone's actual rights. The alleged right-of-way and other institutional examples are scoped to the D4 design exercise. `register-lexicon-ceilings.md:180-183` uses “language games” for linguistic transformations, not video-game mechanics.
- The two entries are reference documents, not complete §4 transfer envelopes. That is not a conformance failure absent a requested handoff; the contract's receipt and canon gates still apply before any import.

## Entry/index and source-resolvability results

At 2026-10-18T21:02:16Z, this command exited 0:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/entry-audit.py --json \
  --new corpus/knowledge/linguistics/register-lexicon-ceilings.md \
  --new corpus/knowledge/linguistics/register-strata-attestation.md
```

Both named entries pass the admission bar, are not filler, have all source bullets with locators (`11/11` and `19/19`), have no unresolved local references, digest mismatches, or unresolved couplings, and have clean index rows. The same receipt reports `entries=201`, `index_failing=[]`, and `bar_failing_count=184`. Those 184 are legacy entries missing a newer admission bar, which the audit defines as non-retroactive; they are not failures of these new targets or of the hard index check.

At 2026-10-18T21:02:17Z, the following offline X63 command exited 1 because it correctly reported four non-reproducing quoted sweeps (not because it could not evaluate either entry):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/x63-entry-source-resolvability.py \
  --offline --json --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede
```

That receipt measured 25 resolved local locators and zero unresolved for `register-lexicon-ceilings.md`; it had no local digest pins and listed two URLs as not attempted in offline mode. For the amended `register-strata-attestation.md` it measured 46 resolved local locators, zero unresolved, three URLs not attempted in offline mode, and four source pins re-derived without drift. The amendment check preserved all 313 baseline lines, inserted 123 lines, rewrote/deleted zero, and passed append-only. Each entry has five quoted sweeps (ten total); six reproduced and the following four were classified against the declared round-28 baseline:

| Entry / quoted sweep | Current hit(s), excluding the audited entry | Baseline result | Classification |
|---|---|---|---|
| `register-lexicon-ceilings.md` — `lexicon ceiling` | `register-strata-attestation.md` | no hit | sibling landing |
| `register-lexicon-ceilings.md` — `which semantic fields` | `register-strata-attestation.md`; `sound-symbolism.md` | `sound-symbolism.md` already matched | authoring defect |
| `register-strata-attestation.md` — `attestation register\\|attestation speech` | `register-lexicon-ceilings.md` | no hit | sibling landing |
| `register-strata-attestation.md` — `register law\\|register-law` | `register-lexicon-ceilings.md` | no hit | sibling landing |

The authoring defect is concrete: the quoted absence sweep for `which semantic fields` was already contradicted at the baseline by `sound-symbolism.md:106`, which says to “assign which semantic fields carry ideophones.” The ceilings-entry `lexicon ceiling` sweep was clean at baseline and became false only when the sibling amendment landed. The two strata-entry sweeps likewise became false only after the ceilings entry landed. These are not four equivalent authoring errors: X63's baseline-aware classifier distinguishes one false-at-authoring claim from three later sibling landings. The finding remains uncorrected in the corpus because only this report is in scope.

## Source substance checked and limits

The offline X63 receipt above checks local path resolution, pins, and sweeps; it does **not** fetch the listed URLs or establish source merits. Separate source checks on 2026-10-18 found:

- The [LINGUIST List review of Dixon (2020)](https://linguistlist.org/issues/32/1859/) supports the entry's calibration that Jalnguy is more accurately associated with cross-cousin avoidance in initiation contexts; it also describes replacement lexical content with grammar retained and many-everyday-to-one-Jalnguy correspondence.
- The [Stanford Encyclopedia of Philosophy entry on Speech Acts](https://plato.stanford.edu/entries/speech-acts/) supports the cited distinction between misfires and abuses and the relevance of authority and uptake. The [Social Institutions entry](https://plato.stanford.edu/entries/social-institutions/) discusses constitutive-rule accounts and the Guala/Hindriks objections the knowledge entry flags as contested. These are theoretical sources, not rulings on actual rights.
- The [Internet Archive catalogue for Rappaport's book](https://archive.org/details/ritualreligionin0000rapp) supports bibliographic and chapter-list details only. It does not verify the invariance argument; the entry properly attributes that argument through `corpus/knowledge/myth-symbol/ritual-liminality.md:112` and says the book wording was not retrieved.
- The direct Gotowski PDF locator failed content extraction on this check. The [article HTML page](https://journals.lib.unb.ca/index.php/la/article/view/29638) was retrievable and its abstract supports the broad claim that Verlan permits only certain reversal patterns. The abstract does not independently verify the entry's specific three attested orders or its written-records caveat; those details remain attributed to the paper rather than independently confirmed by this retrieval.
- Other cited works such as Tambiah, Bourdieu, Clanchy, Aronoff, and Bauer were not independently retrieved in primary form in this pass. Their pathways are locally cited in the entries (including `semantics-pragmatics.md:88-100`, `linguistic-anthropology.md:67,91-109`, and `trade-economy-lexicon.md:121`); this audit verifies those paths and the entries' stated limits, not the complete primary-source merits of every bibliography claim.

**Disposition:** no out-of-province content found; no Province or contract edit; no canon, legal-rights, permission, or game-mechanics ruling. Preserve the one authoring-defect sweep and three sibling-landing findings for the appropriate follow-up; do not describe these entries as accepted by lore or rights-cleared.
