# Round 86 — non-author closure spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Reviewed round: kotodama r86, 2026-11-04. Base `1e6b10a02b93a981b012987c51399d278fe37fa9`; delivered revision `b4cf77ebaf9148ff1375abeacb57e7489e7211c1`. This verifier did not author the round. Two fresh read-only reviewer seats independently inspected claims and source decisions; neither executed lane gates or changed files.

## Conformance

- Real report, not marker: `.ufo/reports/round-86/kotodama.md` names two checkable claims, committed changes, LOG items, measurements, Sources & frontier, trends, and four author-asserted SHONEN lines under the required heading. `git log --format='%an %H' -- .ufo/reports/round-86/kotodama.md` returned `kotodama-shokunin ac484445980820c96f6c25a7378cc68c9b570eb5`.
- `scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kotodama-shokunin` returned `branch=main local=b4cf77ebaf9148ff1375abeacb57e7489e7211c1 remote=b4cf77ebaf9148ff1375abeacb57e7489e7211c1 ahead=0 behind=0 head=detached tracked=0 untracked=0`. Lane `git status --porcelain` returned no output before this verifier write.
- `git -C <lane> merge-base --is-ancestor <hash> main` returned 0 for all six report change hashes: `16c267832746e1cb98fb42a56180f8d1d12dc18b`, `079fbf5969e4ac152a360f45cd8ed76a0191e14a`, `8efa380aa3a66aee9d597d9e855e89c807beeea9`, `0e0643b19e5cd46c577a58041fed3cdfedcb51fb`, `3bc22a021a561c9602be60233a397b4298860814`, `b4cf77ebaf9148ff1375abeacb57e7489e7211c1`.
- Prompt sections 1–5 exactly equal the rendered current canonical `kimi-shokunin/templates/round-prompt.md` prefix (Python placeholder substitution and `prompt.startswith(rendered.rstrip())` returned `True`). Includes mission/axes, distinct claims, L2 floor, report path/SHONEN/citations, commit-before-report, push/write scope and L0. Host route amendments are explicit; answering models are not inferred.
- Committed wave evidence reviewed by independent reviewer: twelve settled nonempty outputs, three attack seats (25%), one connector, no replacement/residual/dead seat; WAVE-DONE precedes report. The L1-held planner versus canonical L2-planner conflict remains disclosed debt, not an authorized exception.
- Census command actually run by this integrator: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` returned exit 0 and final `kotodama\tok\t/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`. Existing W01 tier-C/mined and W04 duplicate-URL warnings persist; S927/S928 add cross-scope duplicate-URL warnings, not errors.

Dispatch/completion digest (copied from assigned immutable digest of mutable driver log):

```text
2026-11-04T12:30:55-03:00 launch kotodama round=86 pgid=22209 driver=hyaku-inline attempt=1
2026-11-04T15:16:23-03:00 complete kotodama round=86; hyaku-inline attempt=1
```

## Claim re-checks: re-measured versus evidence-verified

No sibling gate, selftest, counter, or auxiliary probe was executed. Plain Git-object/Python census measurements and source reopening were performed; executable behavior was evidence-verified under PROTOCOL Gate standard.

Reproducible committed-byte census used by the integrator (run in lane; BASE/AFTER are the full hashes above):

```python
import subprocess, re, collections
for rev in (BASE, AFTER):
    paths = subprocess.check_output(['git','ls-tree','-r','--name-only',rev]).decode().splitlines()
    text = subprocess.check_output(['git','show',rev+':corpus/SOURCES.md']).decode()
    rows = [x.strip().strip('|').split('|') for x in text.splitlines()
            if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|',x)]
    print(rev, sum(p.startswith('corpus/knowledge/') and p.endswith('.md') for p in paths),
          len(rows), dict(collections.Counter(r[3].strip() for r in rows)),
          dict(collections.Counter(r[7].strip() for r in rows)))
```

Observed base: knowledge 259; rows 847; A=504/B=322/C=21; mined=748/queued=58/rejected=41. Delivered: knowledge 260; rows 852; A=504/B=326/C=22; mined=752/queued=58/rejected=42. Comparing ID-keyed complete registry lines returned `old registry rows altered 0 new rows 5`. Both D entry and O tool absent in base, present in delivered tree.

### D / depth — improved, verifies

- Plain `git cat-file -s 3bc22a021a561c9602be60233a397b4298860814:corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md` gives 18351. Independent integrator `len(git show AFTER:<entry> bytes)` gives 18351. Counting `^## ` gives eight sections; direct table read gives six substantive decisions (uptake, attestation, selection, editorial intervention, competing solutions, creative ownership). Independent reviewer counted fourteen actual short quotation anchors: 4 S924, 5 S925, 5 S926. Counter shape count 17 includes three URL bullets and is not seventeen quotations.
- `git rev-parse <D-lands>:<entry>` equals delivered entry blob; the measured dossier survives unchanged. Nearest older orality knowledge already covers these genres: this is deepening, not first coverage.
- Committed `reports/round-86/lands-d-corrected.txt` stamps D lands `3bc22a021a561c9602be60233a397b4298860814`, tree `d84d18ece857eceb9cd7c54e5d5dbd6fafb14be2`, counter SHA `15cf54126850d7f16acaec1cc22174a4a6319107752c7b9ee6028473158f19fe`, PASS 7/7, exit 0. Tree identity checked by reviewer. Original OCR red and corrected 14/14 source-span evidence are preserved, not rewritten.
- Gate evidence: `counter-selftest.txt` records eight actual-D-CLI checks, clean green first, named failure IDs and exit expectations. `measurement-record.json` explicitly binds its originally unstamped digest. Freeze and delivered counter SHA256 independently recomputed equal the exact SHA above; claims remain byte-frozen. Controls record freeze-as-lands D FAIL 3/7, missing entry; unchanged base refused exit 2, not falsely called a semantic red.

### O / operability capability — improved, verifies

- Plain committed-object existence: absent at base; delivered tool present. Independent reviewer `git cat-file -s <O-lands>:tools/check-paragraph-locator.py` returned 10396 bytes. `git rev-parse <O-lands>:<tool>` equals delivered tool blob (also checked directly by integrator).
- Committed `lands-o.txt` stamps `8efa380aa3a66aee9d597d9e855e89c807beeea9`, tree `dea15a9af4ec1d9d0c074fcc6e47e1dcf78af18d`, identical frozen counter SHA, PASS 8/8 exit 0. SELFTEST PASS 29 checks; reviewer counted 29 named receipt checks and 29 source invocations. Same Iron quote/capture: expect 1 → FAIL ordinal=2 exit 1; expect 2 → PASS ordinal=2 exit 0. HELDOUT and registry legs pass in committed receipt. Freeze-as-lands O FAIL 2/8 because tool absent.
- Independent code-read confirms declared trusted-local-HTML CLI, exactly-one containing paragraph, inline/whitespace folding, declared navigation/caption exclusions, distinct 0/1/2 outcomes and PARAGRAPH_ERROR refusal. No untrusted-resource/browser-CSS guarantee inferred. Iron source independently reopened and its article paragraph 2 confirmed.
- SKILL registry contains the required gate/probe schema fields. No mutable fleet artifact is graded by this claim, so the extra mutable-fleet snapshot/digest requirement is not triggered; input captures and revision-stamped runs are committed lane evidence.
- Corrected independent overlays in `separability-corrected.txt` record 0 findings / 2 runs / 0 skipped. Pre-dispatch absent-land exit 2 is not a separability pass. Counter weaknesses remain real: a fake reader/selftest, empty decision cells and duplicate source IDs can survive. Here the actual implementation and substantive dossier were independently read; this does not certify the instrument universally.

## Per-axis verdicts

| Axis | Verdict | Evidence |
|---|---|---|
| depth | improved | D re-measurement and source-scoped six-decision dossier; frozen 7/7 evidence |
| operability | improved | O new CLI, 29-check committed selftest and frozen 8/8 positional red/green |
| coverage | unchanged | No first-genre claim; existing ground deepened; PROVINCE unchanged |
| freshness | unchanged | Round-11 L0 pause preserved; no sweep claimed |
| calibration | improved | S927 corrects ordinal; S928 corrects overbroad descriptor; QUALITY 33 grounded in observed disagreement and red/green |
| adjacency | unchanged | NON-CANON handoff; no lore/chousa/kotoba ownership absorbed |

`git diff BASE AFTER -- SCORECARD.md` reviewed: explicit provisional capability, measured D/O revisions, unchanged paused axes and counter limitations; no invented numeric expertise delta. `git diff --name-only BASE AFTER -- corpus/knowledge/ PROVINCE.md` returned only the new D entry. No prior knowledge or PROVINCE alteration; all 847 prior registry rows identical. No owned axis harmed. No exploratory claim declared.

## Outside discernment spot-check

Sources reopened by fresh non-author reviewer, not by the lane. URLs below are the actual source URLs; S925/S926 were reopened as committed local captures, not claimed as fresh network requests. All access for this closure: 2026-11-04.

| Item | Decision | Re-opened source and located quote | Agreement | Reason |
|---|---|---|---|---|
| S924 | admit B/mined | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Proverb, direct reader succeeded; first article paragraph: “of which none has met with universal acceptance.” (9 words) | agree | Dated definitional disagreement, not a universal current definition |
| S925 | admit B/mined | `reports/round-86/evidence/S925.txt:32-80`, Preface p. vii, lines 52–53: “the historical method of treatment can only give an approximation to accuracy.” (12 words); original https://archive.org/download/in.ernet.dli.2015.120981/2015.120981.English-Proverbs-And-Proverbial-Phrases-A-Historical-Dictionary_djvu.txt | agree | Context distinguishes literary appearance, earlier circulation and editorial exclusions; not invention dating |
| S926 | admit B/mined | `reports/round-86/evidence/S926.txt:3750-3780`, Introduction IV p. lxxxiii: “The solution of riddles is too uncertain a matter” (9 words); original https://archive.org/download/riddlesofexeterb00tuppuoft/riddlesofexeterb00tuppuoft_djvu.txt | agree | Following prose allows different folk solutions; no modern consensus/typography inference |
| S927 | admit B/mined correction | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Iron, direct reader succeeded; article paragraph 2: “giving origin to the three important varieties: cast iron, steel, wrought iron.” (12 words) | agree | Span present but opening-paragraph locator false; correction correctly separates presence from position |
| S928 | reject C | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Bronze_Age, direct reader succeeded; opening article paragraph: “metallurgy was taught to men who no sooner recognized the nature and malleable properties of copper” (16 words) | agree | Reject as neutral modern teaching, not absent quote. Text says most races, allows overlap/local chronology, and advances external diffusion; universal descriptor was overbroad |

## Learning trends and decision

- expansion: **improved** — demonstrated new paragraph-locator capability, not source-row inflation or first proverb/riddle coverage.
- quality: **unchanged** — older knowledge remains untouched; same-round OCR correction does not establish older-entry re-verification or supersession.
- discernment: **improved** — outside sample agrees with admits and reject; previous locator disagreement becomes grounded QUALITY 33, and Bronze Age correction preserves the text's qualifications.

**status=ok; admitted=true; verdict=admitted.** Both declared claims verify through plain re-measurements plus committed gate evidence and independent semantic inspection; no axis harmed. Weak general instrument kill-power is not falsely upgraded into a universal capability. SHONEN evidence is inspectable, but this is not a full promotion review: hypothetical creative exercises do not alone establish a real world-bible handoff, and known instruction/counter conformance gaps persist. No boxes checked and no promotion/mint performed.

## Routed defects / next-round obligations

- R86-C1 → kotodama: carry numeric 0–10 mapping/lowest-non-retired-axis demonstrability debt forward; present verdict-only evidence honestly until resolved.
- R86-C2 → kotodama: in a newly declared freeze, strengthen substitute-tool/fake-selftest, empty decision-cell and duplicate-source-ID counter controls; preserve current frozen predicates and survivor evidence. R85-C2 remains partial, not closed.
- R86-C3 → kotodama: future cheapest no-work controls must be committed before freezing; r86 controls were after freeze but before dispatch. Preserve absent-land separability refusal as such, never backdate later overlays.
- R86-C4 → operator/protocol via kotodama L0: resolve canonical L2 planner versus validator prohibition; L1 mapping remains disclosed conflict, not self-waived exception.
- R86-C5 → kotodama/protocol artifact owner: inherited full cited-record red points to two scratch references in unchanged non-author r84 spotcheck; lane must not rewrite verifier-authored history. Carry durable routing, not a false all-green claim.
- R86-C6 → kotodama: extra same-page Wayback coverage for S925/S926 unresolved (429/403 with positive control), not absence; keep source-scope/availability caveat until resolved. S927/S928 inherited Wayback links likewise not falsely represented as newly reopened.

All listed conformance defects are status-neutral; none is a fabricated harm or marker predicate. No tools installed or upgraded for this closure.
