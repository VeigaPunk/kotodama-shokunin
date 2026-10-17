# Phonology sanity gate: inventory, phonotactics, markedness, and allophony

- topic: An executable, bounded verification specification for fictional spoken-language profiles; distinguish contradictions from typological rarity and keep historical/register strata separate.
- sources: Ian Maddieson (2013), “Consonant Inventories”, “Vowel Quality Inventories”, “Voicing in Plosives and Fricatives”, “Front Rounded Vowels”, “Syllable Structure”, and “Absence of Common Consonants”, in Matthew S. Dryer & Martin Haspelmath (eds.), *The World Atlas of Language Structures Online* (Leipzig: Max Planck Institute for Evolutionary Anthropology), chapters linked below; Steven Moran & Daniel McCloy (eds.) (2019), *PHOIBLE 2.0* (Jena: Max Planck Institute for the Science of Human History), https://phoible.org/; Bruce Hayes (2009), *Introductory Phonology*, first edition, Wiley-Blackwell (contrast, distribution, and ordered-rule framework).
- couples: language — `../linguistics/phonetics-phonology.md`, `historical-linguistics.md`, `writing-systems.md`, `naming-systems.md`, `morphological-typology.md`, `language-contact.md`, `sociolinguistics-registers.md`; myth/symbol — `../myth-symbol/symbolism-synthesis-method.md`; era/costume — `../culture-material/era-periodization-models.md`, `garment-lexicon-crosslinguistic.md`, `ritual-garments.md`; sibling handoff — lore-shokunin owns world-bible canon, not this gate.

## 1. Contract and verdicts

- Unit of evaluation: ONE language variety × era/stage × register × lexical stratum, identified in `scope`; do not pool ancestral liturgy, contemporary vernacular, and unadapted loans.
- `/ /` denotes phonemic representation; `[ ]` denotes surface pronunciation. A phonetic output need not be a phoneme. Distinct lexical meanings may share a surface form through neutralization.
- `FAIL / 1 / failed`: a well-formed profile contradicts its declared inventory, legal sequences, or derivations. Report a witness, not “sounds implausible”.
- `REVIEW / 2 / could-not-evaluate`: malformed/unsupported input, unresolved typological prior, inadequate coverage, or an uncompleted wider audit. This is neither a failure of human language nor a clean result.
- `PASS / 0 / clean`: all checks in the explicitly named scope passed. A kernel PASS is NOT a full phonology or canon approval.
- Final full-gate PASS requires the executable kernel plus the inventory, implication-instantiation, boundary/prosody, and provenance audits below; record a named reviewer for the non-kernel checks.
- Design thresholds, fixture sizes, and exit codes here are engineering choices, not linguistic universals. Do not register this document as an installed fleet gate without the separate registry/runner work.

## 2. Input contract: finite segment kernel

Supply one JSON object; the following root keys are required and exhaustive. Strings representing segments are ATOMIC tokens, not characters: `"t͡s"` is one token if the profile analyzes it as one segment.

| Key | Required shape and interpretation |
|---|---|
| `scope` | Nonempty string naming language, stage, register, and native/adapted-loan/liturgical stratum |
| `inventory` | Object with `C` and `V` arrays of distinct phonemic token strings; no overlap; this kernel supports vowel nuclei only |
| `phones` | Unique array of all permitted surface/underlying tokens, including the inventory and every rule source/output |
| `qualities` | Map of every `V` token to its basic height/backness/rounding quality label; length/nasality/phonation alone do not create a new quality |
| `legal` | `ur` and `sr` objects, each with `onset`, `nucleus`, `coda` arrays of allowed token arrays; `[]` permits an empty margin, never an empty nucleus |
| `rules` | Ordered array of `{id,src,dst,left,right}`; one-token substitution; neighboring token, `null` = any context, `"#"` = word edge |
| `examples` | Array of `{id,u,s}`; `u` is a list of syllables, each `[onset,nucleus,coda]`; `s` is the expected flat surface-token array |
| `priors` | Array of `{id,if_any,all,any}`; trigger if an `if_any` token is phonemic; require every `all` token and at least one `any` token when that list is nonempty |

- Normalize IPA token spellings to Unicode NFC; do not split combining marks, aspiration diacritics, affricates, or prenasalized segments by code point. `g`/`ɡ` aliases need an explicit canonicalization decision, not silent substitution.
- Expand natural-class rules into finite contextual rules for this kernel; list the class definition and expansion in the review record. Missing expansion is REVIEW, not permission to ignore a rule.
- Exhaustive role whitelists are this implementation's representation, not a claim that a real grammar stores syllables as lists. A supplied parse is a legality witness; rejecting that parse does not prove that no alternative parse exists.
- Required wider audit: syllabic consonants, tone/stress, harmony, moras, epenthesis/deletion, optional or probabilistic rules, morpheme boundaries, and cross-word sandhi are outside the kernel. If present but untested, overall verdict remains REVIEW.

## 3. Inventory versus typology audit

Framework: compare phonemic inventories, not spelling alphabets or the union of all surface phones. WALS and PHOIBLE encode analyses of particular documented varieties, not immutable totals for language names.

| Measure | Comparison bands / rule | Gate action and source |
|---|---|---|
| Consonant count | 6–14 small; 15–18 moderately small; 19–25 average; 26–33 moderately large; ≥34 large | Descriptive labels, not admission thresholds; outside an observed sample range requires investigation, never automatic rejection; [Maddieson 2013, ch. 1](https://wals.info/chapter/1) |
| Basic vowel qualities | ≤4 small; 5–6 average; ≥7 large | Count `/i iː ĩ/` as one quality ONLY if their basic timbre is the same; separately report total phonemic vowel contrasts; [Maddieson 2013, ch. 2](https://wals.info/chapter/2) |
| Simple syllables | `(C)V` | NOT the same as `CV(C)`; [Maddieson 2013, ch. 12](https://wals.info/chapter/12) |
| Moderately complex syllables | Coda of at most one consonant and/or restricted CC onset, typically second member liquid/glide | A template `CCVC` can be moderate; inspect allowed combinations, not just maximum length; ch. 12 |
| Complex syllables | Freer CC onsets, ≥3 onset consonants, and/or ≥2 coda consonants | Count morphological edge clusters separately where appropriate; ch. 12 |
| Inventory balance | No compulsory consonant/vowel compensation | Ch. 2 does not support “few consonants must mean many vowels”; do not manufacture a complexity budget |

Inventory audit procedure: chart place × manner × laryngeal contrast, then vowel height × backness × rounding; annotate length, phonation, nasalization, and marginal/loan status separately. Check every cell against lexical contrasts or a declared fictional contrast test.
- A missing `/p/` in a stop series or a lone unusual sound is NOT inherently a contradiction; symmetry is a useful design prior, not a mandatory grid-filling rule.
- Affricate-versus-cluster and long-vowel-versus-sequence analyses change counts and legality together: rerun both checks after changing the analysis.
- PHOIBLE may contain disagreeing inventories for one language. Record inventory identifier AND underlying grammar/source; do not majority-vote duplicate descriptions into independent evidence.

## 4. Markedness: instantiate implications as reviewable priors

Markedness may mean frequency, structural complexity, acquisition, or phonetic difficulty; these are not interchangeable measures. The following are statistical/analytical prompts, not hard universals.

| Prior ID | Trigger → expected comparison | Calibration / disposition |
|---|---|---|
| `M-ROUND` | Front rounded vowel → inspect front unrounded and back rounded vowels of similar height | Usually co-occurs, not guaranteed; instantiate e.g. `y → i,u`; ch. 11 explicitly says “in most cases”; [Maddieson 2013](https://wals.info/chapter/11) |
| `M-VOICE` | Voiced fricatives → inspect presence of voiceless fricatives | Do NOT require a voiceless counterpart at every identical place; ch. 4 documents inventories with only voiced fricatives; [Maddieson 2013](https://wals.info/chapter/4) |
| `M-NASAL` | Nasal consonant → inspect oral consonants at that place | Exception-aware: ch. 18 discusses Aleut's bilabial nasals without bilabial oral stops/fricatives; [Maddieson 2013](https://wals.info/chapter/18) |
| `M-CLASS` | No phonemic nasals, fricatives, or bilabials → inspect analysis and allophones | Such absences are attested; a language with nasal phones need not have nasal phonemes; ch. 18 |
| `M-SONORITY` | Complex onset → inspect tendency to rise toward nucleus | Sonority sequencing is an analytical heuristic, not a universal ban; special `/s/+stop` licensing or another explicit analysis may be needed; Hayes 2009 |

- Implement finite positive implications with `priors`; instantiate all applicable peers from the chart, not just IPA letter lookalikes. `M-CLASS` absence checks and sonority need the wider audit, not fake positive triggers.
- Failed prior → REVIEW with source, analysis, and a design rationale; never silently insert “missing” phonemes. An accepted exception remains visible in the handoff.
- Specific popular claim “every voiced fricative entails its voiceless counterpart” is refuted as an absolute by ch. 4. “Every exotic sound needs a full series” is also not a gate rule.
- No inference from inventory to intelligence, moral character, social rank, technological era, pantheon, or climate. Anecdotal climate/anatomy explanations are `(to-verify)` unless independently sourced for that claim.

## 5. Legality and allophony audits

| Check | Required execution | Finding |
|---|---|---|
| Inventory membership | Every underlying token must be a phoneme of this scoped stratum | `I-UNKNOWN`, FAIL |
| Syllable roles | Every supplied onset/nucleus/coda must occur in its layer's whitelist | `P-UR` or `P-SR`, FAIL; preserve offending word, syllable, role |
| Cross-syllable restrictions | Test banned sequences/harmony over the whole word, not each syllable independently | Wider audit; untested restrictions = REVIEW |
| Morphology/contact | Test stem + each productive affix and representative compounds/loans | Illegal derived cluster needs an explicit licensed boundary or repair; a bare template does not license everything |
| Rule semantics | In array order, take a snapshot; rewrite all matching positions simultaneously once; next rule sees the resulting string | No repeat-until-stable; no unordered rewriting |
| Rule coverage | At least one triggering site per rule; conditioned rules also need a blocked site with the same source segment | `A-COVER`, REVIEW; unconditional rules need no impossible blocked witness; fixture policy, not a linguistic universal |
| Derivation | Predicted surface must equal the supplied token sequence exactly | `A-DERIVE`, FAIL; record ordered trace during wider review |
| Surface roles | One-to-one rules retain input role spans; resulting role tokens must be licensed in `sr` | `P-SR`, FAIL; insertion/deletion needs a different syllabification engine |
| Contrast analysis | Compare lexical meanings, environments, stress, boundaries, and register before merging categories | Complementary distribution alone does not prove two phones are one phoneme; Hayes 2009 |

- Feeding: R1 creates an R2 environment; bleeding: R1 removes one. Check both orders on an interacting witness; the declared order, not an aesthetic preference, determines the expected result.
- Ordered overlap is not automatically inconsistent. Undeclared choice between distinct outputs is REVIEW; supplying an output incompatible with the declared deterministic order is FAIL.
- Free variation and sociolinguistic variants require explicit alternative profiles or a richer evaluator; do not declare two variants contradictory merely because both occur.
- Allophone neutralization into another phoneme's usual phone is permitted. A phonemic distinction claimed in the SAME conditioning context still needs a contrast witness or reanalysis.

## 6. Runnable reference kernel

Python 3 standard library only; read-only, no network, no random sampling. Its result has `scope=finite-segment-kernel`; the wider audit remains obligatory. Malformed JSON is a CLI input error; malformed profile shape becomes `G-DATA` REVIEW. No files are generated.

```python
import copy, json, sys, unicodedata

def evaluate(d):
    findings, counts = [], {}
    def add(level, code, witness):
        findings.append({"level": level, "id": code, "witness": witness})
    try:
        required = {"scope", "inventory", "phones", "qualities", "legal", "rules", "examples", "priors"}
        if set(d) != required or not isinstance(d["scope"], str) or not d["scope"].strip():
            raise ValueError("root keys or scope")
        if not all(isinstance(d[k], list) for k in ("rules", "examples", "priors")): raise ValueError("record arrays")
        for k, keys in (("rules", {"id","src","dst","left","right"}), ("examples", {"id","u","s"}), ("priors", {"id","if_any","all","any"})):
            if any(not isinstance(row, dict) or set(row) != keys or not isinstance(row["id"], str) or not row["id"] for row in d[k]): raise ValueError("record shape or id")
        for w in d["examples"]:
            if not isinstance(w["u"], list) or not isinstance(w["s"], list) or not all(isinstance(x, str) for x in w["s"]): raise ValueError("example arrays")
            if any(not isinstance(s, list) or len(s) != 3 or any(not isinstance(part, list) or not all(isinstance(x, str) for x in part) for part in s) for s in w["u"]): raise ValueError("syllable arrays")
        for prior in d["priors"]:
            if any(not isinstance(prior[k], list) or not all(isinstance(x, str) and x for x in prior[k]) for k in ("if_any", "all", "any")): raise ValueError("prior token arrays")
        if set(d["inventory"]) != {"C", "V"} or set(d["legal"]) != {"ur", "sr"}: raise ValueError("inventory/layer keys")
        cs, vs, phones = d["inventory"]["C"], d["inventory"]["V"], d["phones"]
        if not all(isinstance(xs, list) for xs in (cs, vs, phones)):
            raise ValueError("token arrays required")
        if not all(isinstance(x, str) and x and x != "#" for x in cs + vs + phones):
            raise ValueError("nonempty segment strings; # reserved")
        p, allowed = set(cs + vs), set(phones)
        if len(p) != len(cs + vs) or len(allowed) != len(phones):
            add("FAIL", "I-DUPLICATE", "inventory overlap or duplicate token")
        if len({unicodedata.normalize("NFC", x) for x in phones}) != len(allowed):
            add("FAIL", "I-ALIAS", "distinct tokens normalize to the same IPA")
        if any(unicodedata.normalize("NFC", x) != x for x in phones):
            raise ValueError("canonicalize all tokens to NFC")
        if not p <= allowed or set(d["qualities"]) != set(vs):
            raise ValueError("inventory/phone/quality coverage")
        if any(not isinstance(q, str) or not q for q in d["qualities"].values()): raise ValueError("quality labels")
        counts = {"C": len(cs), "V_phonemes": len(vs), "V_qualities": len(set(d["qualities"].values()))}
        legal, rules = d["legal"], d["rules"]
        for layer in ("ur", "sr"):
            if set(legal[layer]) != {"onset", "nucleus", "coda"}:
                raise ValueError("legal role keys")
            for role, options in legal[layer].items():
                if not isinstance(options, list): raise ValueError("role options must be arrays")
                for option in options:
                    if not isinstance(option, list) or not set(option) <= (p if layer == "ur" else allowed):
                        raise ValueError("undefined legality token")
                    if role == "nucleus" and not option:
                        raise ValueError("empty nucleus")
                    if layer == "ur" and not set(option) <= set(vs if role == "nucleus" else cs):
                        raise ValueError("underlying role class")
        if len({r["id"] for r in rules}) != len(rules):
            raise ValueError("duplicate rule id")
        for r in rules:
            if not {r["src"], r["dst"]} <= allowed:
                raise ValueError("undefined rule segment")
            if any(r[k] is not None and r[k] != "#" and r[k] not in allowed for k in ("left", "right")):
                raise ValueError("unsupported rule environment")
        coverage = {r["id"]: [False, r["left"] is None and r["right"] is None] for r in rules}
        used = set()
        if not d["examples"] or len({w["id"] for w in d["examples"]}) != len(d["examples"]):
            raise ValueError("missing examples or duplicate example id")
        for w in d["examples"]:
            if not w["u"] or any(not syllable[1] for syllable in w["u"]):
                raise ValueError("syllable triple or nucleus")
            spans = [(n, role, part) for n, syllable in enumerate(w["u"]) for role, part in zip(("onset", "nucleus", "coda"), syllable)]
            ur = [x for n, role, part in spans for x in part]
            if not set(ur) <= p or not set(w["s"]) <= allowed:
                add("FAIL", "I-UNKNOWN", w["id"]); continue
            used.update(ur)
            for n, role, part in spans:
                if part not in legal["ur"][role]: add("FAIL", "P-UR", [w["id"], n, role, part])
            sr = ur[:]
            for r in rules:
                old = sr[:]
                for i, token in enumerate(old):
                    if token != r["src"]: continue
                    left, right = old[i-1] if i else "#", old[i+1] if i+1 < len(old) else "#"
                    match = (r["left"] is None or r["left"] == left) and (r["right"] is None or r["right"] == right)
                    coverage[r["id"]][0 if match else 1] = True
                    if match: sr[i] = r["dst"]
            if sr != w["s"]: add("FAIL", "A-DERIVE", [w["id"], sr, w["s"]])
            cursor = 0
            for n, role, part in spans:
                surface_part = sr[cursor:cursor+len(part)]; cursor += len(part)
                if surface_part not in legal["sr"][role]: add("FAIL", "P-SR", [w["id"], n, role, surface_part])
        if p - used: add("REVIEW", "I-COVER", sorted(p - used))
        for rid, evidence in coverage.items():
            if not all(evidence): add("REVIEW", "A-COVER", [rid, evidence])
        for prior in d["priors"]:
            if p & set(prior["if_any"]) and (set(prior["all"]) - p or (prior["any"] and not p & set(prior["any"]))):
                add("REVIEW", prior["id"], "expected comparison absent; not a universal")
    except (KeyError, TypeError, ValueError, IndexError, AttributeError) as error:
        add("REVIEW", "G-DATA", str(error))
    code = 1 if any(f["level"] == "FAIL" for f in findings) else 2 if findings else 0
    return {"scope": "finite-segment-kernel", "profile": d.get("scope") if isinstance(d, dict) else None,
            "exit": code, "verdict": {0: "PASS", 1: "FAIL", 2: "REVIEW"}[code], "counts": counts, "findings": findings}

def fixture():
    c, v = list("ptkmns"), list("iau")
    ur = {"onset": [[]] + [[x] for x in c], "nucleus": [[x] for x in v], "coda": [[]]}
    sr = copy.deepcopy(ur); sr["onset"].append(["t͡s"])
    words = [("p", "a"), ("t", "i"), ("k", "u"), ("m", "a"), ("n", "a"), ("s", "a"), ("t", "a")]
    return {"scope": "fixture-only/E0/ordinary/native", "inventory": {"C": c, "V": v}, "phones": c + v + ["t͡s"],
            "qualities": {"i": "high/front/unrounded", "a": "low/central/unrounded", "u": "high/back/rounded"},
            "legal": {"ur": ur, "sr": sr}, "rules": [{"id": "R1", "src": "t", "dst": "t͡s", "left": None, "right": "i"}],
            "examples": [{"id": str(i), "u": [[[a], [b], []]], "s": ["t͡s" if (a,b) == ("t","i") else a, b]} for i, (a,b) in enumerate(words)],
            "priors": [{"id": "M-ROUND", "if_any": ["y"], "all": ["i", "u"], "any": []}]}

def selftest():
    cases = [(fixture(), 0, None)]
    def case(code, finding, mutate):
        d = fixture(); mutate(d); cases.append((d, code, finding))
    case(1, "A-DERIVE", lambda d: d["examples"][1].update(s=["t", "i"]))
    case(1, "P-UR", lambda d: d["legal"]["ur"]["onset"].remove(["p"]))
    case(1, "P-SR", lambda d: d["legal"]["sr"]["onset"].remove(["t͡s"]))
    case(1, "I-UNKNOWN", lambda d: d["examples"][0].update(s=["x", "a"]))
    case(2, "A-COVER", lambda d: d["examples"][1].update(u=[[[], ["i"], []]], s=["i"]))
    case(2, "M-ROUND", lambda d: d["priors"].append({"id":"M-ROUND", "if_any":["i"], "all":["y"], "any":[]}))
    case(2, "G-DATA", lambda d: d.pop("scope"))
    for d, expected, fid in cases:
        result = evaluate(d)
        assert result["exit"] == expected, result
        assert fid is None or fid in {f["id"] for f in result["findings"]}, result
    print("self-test: 8/8; exit and finding-id expectations matched")

if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]: selftest()
    else:
        try: result = evaluate(json.load(sys.stdin))
        except (json.JSONDecodeError, UnicodeError) as error:
            result = {"scope":"finite-segment-kernel", "exit":2, "verdict":"REVIEW", "findings":[{"id":"G-DATA", "witness":str(error)}]}
        print(json.dumps(result, ensure_ascii=False, sort_keys=True)); sys.exit(result["exit"])
```

Run from the lane root, extracting the sole Python fence into memory; replace `--self-test` with stdin redirection `< profile.json` to evaluate an authorized input profile:
`python3 -c 'from pathlib import Path; p=Path("corpus/knowledge/verification/phonology-sanity-gate.md"); exec(compile(p.read_text().split("```python\n",1)[1].split("\n```",1)[0],str(p),"exec"))' --self-test`
The `M-ROUND` negative self-test deliberately injects a false synthetic prior to test routing; it does NOT assert that `/i/` implies `/y/`. Fixtures are method demonstrations, never setting vocabulary or canon.

## 7. Era staging, coupling, and full-gate handoff

| Surface | Stage-sensitive test | Coupled craft consequence |
|---|---|---|
| Older liturgy / divine epithets | Run the older profile, then the ordered change chain into the present vernacular | An archaic theonym may be legal in its source register without enlarging every modern speaker's inventory |
| Script / emblem | Compare spelling history with phonemic analysis; test names without decorative punctuation | One rune, letter, or emblem is not automatically one phoneme; an apostrophe cannot supply a missing contrast |
| Garment / craft loan | Test donor form, adapted form, and productive suffixation under their own scopes | Textile-trade vocabulary can preserve a contact layer; material technology does not determine a sound inventory |
| Ritual mask / performance | Separate acoustic filtering and deliberate performance register from community phonemic contrast | Do not infer permanent phoneme loss from mouth coverings; any empirical mask/acoustics claim needs its own evidence `(to-verify)` |

Full-gate record: profile identifier + immutable input digest; reviewer; kernel exit/findings; phoneme and quality counts; inventory chart; instantiated-prior list and accepted exceptions; legality witnesses; ordered derivations; positive/blocked rule sites; boundary/prosody audit; source editions and unresolved `(to-verify)` items. Record input hash with the actual authorized run, not a fabricated example hash.

## 8. What a worldbuilder can take; provenance cautions

- Take a repeatable chart → legality model → ordered-rule derivation → contrast audit, not a “civilized/barbaric” sound palette. Test personal names, place names, theonyms, and costume terms through the SAME scoped system.
- For a naturalistic profile, repair contradictions first; then decide consciously whether unusual patterns are worth the extra explanation. Lore-shokunin receives options, exceptions, and uncertainty; only that sibling decides canon.
- WALS chapter labels/bands and PHOIBLE's source-disagreement warning were checked against the linked project pages on 2026-10-17. Hayes is a standard textbook citation; exact page-level corroboration of this entry's rule discussion is `(to-verify)`.
- Typological convenience samples are not independent random samples; family, area, documentation, and analytical conventions affect comparisons. Old labels such as “Khoisan” or “Altaic” in a source must not be promoted into accepted genealogical groupings.
- Colonial-era transcription and outsider grammars can miss contrasts or impose familiar categories; keep modern community-informed descriptions and the original analysis side by side when available. No living tradition is represented adequately by an inventory table alone.
- Ancient or poorly documented pronunciation has sparse evidence: spellings, rhymes, loans, and comparative reconstruction support different confidence levels. This entry supplies no civilization-specific reconstruction; any claim about a particular extinct language's allophones remains `(to-verify)` until a specialist source is checked.
