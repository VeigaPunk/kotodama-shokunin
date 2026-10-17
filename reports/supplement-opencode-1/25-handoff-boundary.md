# 25 — Handoff boundary: what the checker's exit 0 proves, and what waits on lore

- wave: `supplement-opencode-1` (not a numbered GLM round)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404` (HEAD; working tree clean apart from untracked `reports/`)
- role: REVIEWER (handoff boundary); no commits, no edits outside this file, no lore/fleet writes
- entry under review: `examples/handoff-packet.sample.md`, sha256 `4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712` (unchanged before/after review)
- scratch: `reports/supplement-opencode-1/scratch/25-handoff-boundary/` (three probe copies only)

## 1. Commands actually executed, and what they returned

| command | observed result |
|---|---|
| `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | `INFO scan: fields=16/16 glossary-entries=20 findings=0`; exit 0 |
| `python3 tools/gates/handoff-packet-check.py --selftest` | `selftest: OK — fixture findings 11 across 9 ids (…); clean control exit 0; probes cover canon, baseline, dependency, contract_ref and glossary vocabulary; malformed inputs exit 2; CLI verified from another cwd`; exit 0 (0.15 s) |
| `cat examples/handoff-packet.sample.md \| python3 tools/gates/handoff-packet-check.py -` | exit 0 (same scan line) — stdin ⊆ file |
| re-run on the file, then `md5sum -c` on the packet and its YAML payload | exit 0 again; both files byte-unchanged (checker is read-only in practice, matching its docstring) |
| `sha256sum` of the packet's three claimed digests | all three match actual bytes: contract `50c4c2f2…68c1`, design record `e96bc943…a2509`, YAML payload `b900549e…02e6` |
| `sha256sum tools/gates/*.py` vs the digests pinned in the YAML `validation` block | all 7 match (handoff `e2fa3223…`, phonology `fb05c644…`, naming `8c5afb0a…`, lexicon `63ee4ec6…`, myth `26d246e9…`, costume `29a9361c…`, provenance `4aaea6e9…`) |
| spot check of manifest counts: `grep -c '^\| L' examples/handoff-packet.sample.md` | 20 → the glossary table really carries L01–L20, matching the A3 count in the `11/4/20/15/19/20/17` series (only A3 is cheaply checkable here) |

## 2. Exactly what exit 0 proves

Exit 0 means **zero findings of any level** (FAIL, REVIEW, or HOLD) from `evaluate_text()` over this one document. Concretely, for this packet:

1. All 16 §4 field names were recognized with at least one non-placeholder occurrence (`collect_fields`, `FIELD_NAMES`, `handoff-packet-check.py:122-160, 274-314`; scan line `fields=16/16`).
2. The §4-adjacent REVIEW checks found nothing: `baseline_bible_ref: none` is accompanied by a deliberate unbound-research declaration (`:507-521`), `contract_ref` carries revision and digest (`:523-535`), `artifact_manifest` carries a file digest (`:537-547`), `dependency_manifest` floats no `latest` (`:549-560`).
3. A non-canon marker (`not canonized` / `not yet canonized`) is present (`CANON_MARKER_RE`, `:171, 562-570`).
4. `canon_claims()` (`:332-355`) matched no producer-side canon certification line.
5. The 20 inline glossary rows each carry an etymology status inside the licensed vocabulary attested/reconstructed/constructed/contested/unknown (`:388-444`).
6. Nothing more. The tool's own docstring states the boundary: it does **not** judge whether the declared checks were really run, whether digests match bytes, whether subject references resolve to lore entities, or whether payload content is good; it cannot open files it was not given. Its field-recognition limit is explicit: a quoted specification table cannot be told apart from the packet's own data.

It is a producer-side document-shape check — contract §8 step 3's "local generation/derivation verification", not §8 step 5 bible-wide verification and not any acceptance.

## 3. What remains pending — the lore-consent boundary

The packet itself is honest about all of this; the checker does not gate on any of it.

- **§1 both-lane read (blocking first transfer).** No read record with `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` exists in this repo; a repo-wide search finds only the requirement text, the packet's own `pending` statements, and `corpus/lessons/round-2-adjacency.md` open question 3 recording the same absence. The packet says it at line 5 and in `contract_ref`, and OQ-08 declares it blocking. The checker has no read-record check, so exit 0 coexists with the gate unmet.
- **§8 step 1 lore-supplied inputs.** OQ-07: no baseline bible, entity keys, or receipt surface supplied. `baseline_bible_ref: none` (unbound research packet, §4) means no canon import is possible without a lore baseline and a new reviewed handoff.
- **§8 steps 5–6 receipt.** No receipt exists; §8 Step 6 requires packet ID/version/digest, contract reference, review baseline, per-record disposition and reason, unresolved blockers, and a reviewer/time/evidence pointer. RD-08 asks what receipt surface and baseline apply before any transfer.
- **§8 step 7 canonization.** Never claimed: the packet's standing is `not canonized — lore disposition required`; §8 step 7 requires a receipt naming approved bible IDs and the resulting bible revision, plus any operator approval, before anything is canonized.
- **§8 step 4 and §6.** Submission, delivery, and silence are never acceptance; canon standing is lore's alone — exit 0 does not move either.
- **Requested decisions.** All 8 (RD-01…RD-08) are pending, and all `subject_refs` are unresolved namespaced candidates.
- **Payload blockers are untouched by the envelope pass.** The YAML validation records five non-clean gate exits for the payload (1 REVIEW phonology A-NEUTRAL; 2 HOLD naming CROSS-HOLD; 4 C-required-gap lexicon; 1 note costume; provenance not applicable). A clean envelope says nothing about them.

## 4. Producer-canon assertion probe (minimal)

Appending one line to a scratch copy of the clean packet flips the verdict:

- list-item form: `- canon_standing: canonized — the producer certifies this packet as canon and grants it world-bible standing.` → `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 156: …`; `fields=16/16 glossary-entries=20 findings=1`; exit 1.
- table form: `| canon_standing | canonized by the producer as approved world-bible canon |` → one HO-CANON-CLAIM at line 154; exit 1.
- negative control: `| lore_disposition | lore may canonize this packet after its own review; no producer certification is made |` → exit 0, no findings. So the check is not a keyword tripwire: pending/lore-side wording stays clean.

Conclusion: the boundary is enforced at the packet-document level (exit 0 ⇔ no producer canon claim present), but enforcement is about the document's wording, not about anyone's actual consent.

## 5. Calibration finding: a recorded checker result that does not reproduce

The YAML payload's `validation` block records, for `handoff-packet-check.py` (digest `e2fa3223…`, which matches current bytes): `exit: 1, findings: "CORRECTED at round-2 close: re-run … exits 1 — this YAML serialization is not the contract-default Markdown the checker recognizes (field-recognition misses, HO-EMPTY/HO-MANIFEST-DIGEST)"`. The round-2 LOG entry repeats that statement.

On the pinned baseline this does not reproduce:

```
$ python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.yml
INFO scan: fields=16/16 glossary-entries=0 findings=0
EXIT_YML=0
```

The reason is visible in the frozen bytes: the YAML carries `envelope_markdown_view:` (lines 42–58) — the same §4 envelope in the `- field: value` form the checker recognizes. Two consequences worth recording:

1. The recorded exit-1 correction is stale or wrong for the committed artifact; the file has a single commit (`1688790`), so history cannot distinguish "stale record" from "record wrong when written".
2. The YAML's exit 0 is weaker than the Markdown packet's: `glossary-entries=0` — the checker's clean run over the YAML verifies **no** etymology rows at all, and the pass relies exactly on the documented false-pass mode (a serialization view inside a document being read as the document's own envelope).

No correction was applied: `examples/*` and the YAML are outside my write surface; the contradiction is reported for the parent/integrator.

## 6. Source rechecks (three claims from this entry)

Verdicts: supported / contradicted / unresolved. Excerpts are short and were actually retrieved; snippet-only and blocked retrieval are not counted as confirmation. Social-search tooling was quota-blocked during this pass, so sources were reached by direct URL (WALS, PMC, DOI/Crossref/OpenAlex probes).

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "examples/handoff-packet.sample.md",
  "entry_sha256_before": "4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712",
  "checked_at_utc": "2026-10-17T15:41:00Z",
  "audits": [
    {
      "id": "S25-A1",
      "claim": "CL02: Japanese SOV/suffixing, English SVO (typological comparator only; Dryer 2013 WALS ch.81, Shibatani 1990)",
      "entry_locator": "claim_ledger table row CL02 (line 48)",
      "source_url": "https://wals.info/chapter/81",
      "retrieval_status": "retrieved (full chapter text)",
      "source_locator": "Dryer, WALS ch.81 'Order of Subject, Object and Verb': opening section, example (2a) Japanese (Kuno 1973:10); example (1)",
      "source_excerpt": "English is SVO (Subject-Verb-Object), because the subject the dog … precedes the verb while the object the cat follows the verb. … a. Japanese (Kuno 1973: 10) John ga tegami o yon-da. … S O V",
      "verdict": "supported (word-order half); unresolved (suffixing half)",
      "basis": "The cited chapter is the word-order map (81A) and its retrieved text gives Japanese as SOV and English as SVO, matching the packet. The 'suffixing' half is not covered by the cited chapter: prefixing vs suffixing is WALS ch.26 (also Dryer), retrieved in full, whose prose gives only regional statements ('preference for suffixes is especially strong on the mainland of Eurasia') and does not name Japanese; the ch.26 per-language datapoint page is JavaScript-rendered and returned no value text. Wrong-fit citation for that half, not a contradiction.",
      "access_limit": "WALS datapoint pages require JS; no per-language ch.26 value retrieved. Search tooling quota-blocked (HTTP 403), so no independent second index was consulted."
    },
    {
      "id": "S25-A2",
      "claim": "CL11/CL08: dress = body modifications and supplements, not garments alone; costume cuts are design choices, no real garment reconstructed (Roach-Higgins & Eicher 1992)",
      "entry_locator": "claim_ledger rows CL11 (line 57) and CL08 (line 54); coupling edges E07/E08 are the design-side users",
      "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10559650/",
      "retrieval_status": "retrieved (full text, PMC open access)",
      "source_locator": "Hester & Hehman 2023, Pers Soc Psychol Rev 27(4):414-433, dress-definition paragraph quoting the cited work with page locator (Roach-Higgins & Eicher, 1992, p. 1)",
      "source_excerpt": "Dress of an individual is an assemblage of modifications of the body and/or supplements to the body. (Roach-Higgins & Eicher, 1992, p. 1) … Makeup and tattoos are dress, despite not being as explicitly \"material\" as clothing.",
      "verdict": "supported",
      "basis": "A peer-reviewed open-access article quotes the cited 1992 definition verbatim with a page locator, and its surrounding discussion states that dress is not limited to material garments — exactly the packet's use. This is the dress↔costume-coupling claim (CL08's 'no real garment reconstructed' rests on the same conceptual stance). Support is via verbatim quotation in the retrieved secondary source.",
      "access_limit": "Publisher full text of Roach-Higgins & Eicher 1992 not retrieved: journals.sagepub.com returned HTTP 403; the packet cites no DOI; a Crossref API lookup for the DOI form tried returned 404 (recorded as a limit of my retrieval, not as a claim that the DOI is wrong). Primary text remains unread."
    },
    {
      "id": "S25-A3",
      "claim": "CL09: rite-of-passage triad used as heuristic, not law (van Gennep 1960 [1909]); coupling edge E14 uses it as an analogy for the D1 passage rite",
      "entry_locator": "claim_ledger row CL09 (line 55); coupling edge E14 (line 89)",
      "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13565038/",
      "retrieval_status": "retrieved (full text, PMC open access)",
      "source_locator": "Wyatt et al. 2026, Perspect Med Educ 15(1):819-829, Methods and 'Rites of passage' paragraph; reference list entry [15]",
      "source_excerpt": "Van Gennep describes rites of passage (i.e. transitions from one social position to another) in terms of three phases: separation, liminality, and aggregation. … [15] van Gennep A. The rights of passage (Trans. by Monika B Vizedom and Gabrielle L Caffee. Routledge and Kegan Paul; 1960.",
      "verdict": "supported",
      "basis": "Retrieved full text of a peer-reviewed article uses the triad as an analytic framework and its reference [15] is the exact 1960 Vizedom & Caffee translation the packet names. The ritual/life-stage framework the packet borrows as a heuristic is real and in scholarly use; the packet's own calibration ('heuristic, not law') is consistent with how the source applies it.",
      "access_limit": "Primary 1960 translation not retrieved (in copyright; Internet Archive full-text endpoint returned HTTP 503). The source demonstrates framework use; it does not test the packet's design application."
    }
  ]
}
```

## 7. Limits of this review, and what is left undone

- Reviewed only the Markdown sample packet, the checker, the contract, and the payload's validation records. No lore repo, no world bible, no sibling lanes were read; no lore consent was sought or assumed.
- Retrieval limits are recorded per audit above (SAGE 403, Crossref 404 for the DOI form tried, WALS JS datapoints, Internet Archive 503, web-search tooling quota-blocked). Nothing blocked was upgraded to a verdict; unretrieved items stay unresolved.
- Left for the parent: (a) whether kotodama should file its own §1 read record before any transfer, and whether the checker should gate on read records (design decision, not taken here); (b) the calibrated/incorrect YAML validation record and its LOG echo (§5) — stale record vs. wrong record cannot be settled from the single-commit history; (c) the CL02 "suffixing" citation-precision item (ch.81 → ch.26), which is a wrong-fit citation in committed baseline bytes — reported, not edited.
