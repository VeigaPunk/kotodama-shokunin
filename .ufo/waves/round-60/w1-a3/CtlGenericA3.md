CONTROL-MET: CtlGenericA3/b-quote (SESSIONS-only probe; frozen FAIL)

# CtlGenericA3 — content-free and shortcut-line controls

## Scope and axes

- Depth: distinguish source-scoped additions from empty sentences, quote-only copying, reused base lines, and repeated citations.
- Detector sensitivity: exercise revision 5 without changing its rules.
- Isolation and reversibility: one scratch clone, bounded synchronous detectors, exact byte restoration after every variant.
- This is a pre-data control receipt, not a support verdict, round judgment, integration decision, or claim-admission report. No actual support reviewer was contacted or dispatched.

Read the declaration first. Cloned the lane with the supplied no-hardlinks command and checked out `14e6413820d482913f723432b62d566967ccd1a6`. Applied `/fast/scratch/hyaku/kotodama-r60a3/L1/build.patch` and copied its `captures/` into the scratch clone. The patched entry matched `L1/candidate-entry.md` byte-for-byte before mutation. Only the four lines citing S648–S651 were replaced (or duplicated for the two-line case); source rows and capture bytes were unchanged.

Scratch: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/`. Frozen counter: `clone/reports/round-60/accept-d.py`, sha256 `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Inherited patch sha256: `e37abc6d6403a26ecaeb8aa6434dba3d3ffd02775a7e53ce9d1c8090a9ef2d61`.

## Detector and fixture construction

The same bounded command was run from the clone for pristine, each mutated, and each restored state:

`timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`

The probe substitutes its absolute filename for the counter filename and otherwise uses the same working directory, environment, input bytes, and deadline. Every caller used `PYTHONDONTWRITEBYTECODE=1`; temporary files and uv/cache directories were under this sandbox. The frozen locator's own unchanged PDF subprocess inherits that environment.

To reach the mechanical and SUPPORT legs rather than merely fail for missing packets, the repository's `build-packets.py` built fresh packets against each pre-data entry variant. Each fixture includes the frozen planted file, a corresponding key hash, a registry, and explicitly marked SYNTHETIC reports/transcripts: real labels are SUPPORTED, planted labels NOT-SUPPORTED, and page-read calls are represented without executing those reads. These are deliberately fabricated test data, not real reviews or evidence of page access. New packets/key hashes are fixture setup before scoring, not post-verdict amendment of a real data object. The baseline support/key bytes are restored after every probe.

Frozen PROVENANCE blocks every synthetic state with `session-files=0`, giving SUPPORT FAIL. Therefore **every overall frozen mutation verdict is inconclusive against the already-failing frozen baseline**, not a claimed killed mutant. The separate probe changes only SESSIONS to matching fake session files under this sandbox, allowing later legs to be tested. Its pristine and all five restored states PASS; its failing mutants can therefore be called killed in that probe. No real session file was created or changed.

### Complete probe diff

```diff
--- reports/round-60/accept-d.py
+++ accept-d-probe.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

Probe sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`. No other counter byte differs.

## Results: mutant, expected detector, output, verdict

| Variant (applied to all four new ids) | Expected detector | Frozen failing legs | Probe failing legs | Probe mutation verdict |
|---|---|---|---|---|
| (a) Generic sentence | ROWS: fewer than 6 quote content words | ROWS, SUPPORT | ROWS | KILLED |
| (b) Row quote copied verbatim | No mechanical rejection; only SUPPORT judges semantic support | SUPPORT | none | SURVIVED / PROBE PASS |
| (c) Adjacent base line plus new id | LINES: normalized base-line reuse; also ROWS: low overlap | LINES, ROWS, SUPPORT | LINES, ROWS | KILLED |
| (d1) New id twice on its one line | LINES counts physical lines, not occurrences | SUPPORT | none | SURVIVED / PROBE PASS |
| (d2) Same cited sentence on two physical lines | LINES: each id has two lines | LINES, SUPPORT | LINES | KILLED |

For **(b), the mechanical legs pass and only SUPPORT judges it**. SET, LINES, OLDWORD, ROWS, PINNED, and JUDGED all PASS in both runs. A verbatim quote satisfies overlap/location without demonstrating a good contextualized repair; the probe's synthetic approvals do not establish a real support judgment. This surviving shortcut is a depth/coverage finding, not permission to change the frozen contract.

The same-line duplicate also passes all six non-SUPPORT legs. The current predicate says exactly one *line* per new id, not exactly one occurrence, so this is an observed allowed shape rather than proof of a contradiction in that predicate. Two physical lines are rejected.

(a) ROWS overlap counts were S648=0, S649=1, S650=0, S651=0. (c) counts were 3, 0, 0, 1; all four also reported `base_line=True`. (d2) reported `lines=2 base_line=False` for each id.

### Exact mutation lines

Each block below is copied from the scored mutant entry artifact. All other entry bytes were left at the inherited candidate, except the four extra duplicate lines in (d2).

#### a-generic

```text
- Amulets were also discussed (S648).
- Amulets were also discussed (S651).
- Amulets were also discussed (S649).
- Amulets were also discussed (S650).
```

#### b-quote

```text
- P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers. (S648).
- was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil. (S651).
- Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649).
- currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck (S650).
```

#### c-base-line

```text
- A palm-sized amulet could itself provide protection from the demon Lamashtu, so the protective object may be small enough to keep in the hand (S603; S648).
- Containment in silver: silver amulet holders, often containing symbolic material or a paper with a magical or holy inscription, were worn throughout the Muslim world (S612; S651). **B**
- White nephrite jade: a Mughal amulet was made to protect the wearer from harm or misfortune and was fashioned in white nephrite jade (S630; S649). **B**
- Carved into the fabric: witches' marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings (S621; S650). **B**
```

#### d-same-line

```text
- Heeßel describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648, S648).
- Ga'u as container: the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil (S651, S651). **B**
- The Met's record says hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649, S649). **C**
- Concealed shoes: Shawcross says the reason why people concealed shoes remains a mystery; University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items, and that they were connected to notions of good luck and hope (S650, S650). **C**
```

#### d-two-lines

```text
- Heeßel describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648).
- Heeßel describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648).
- Ga'u as container: the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil (S651). **B**
- Ga'u as container: the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil (S651). **B**
- The Met's record says hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649). **C**
- The Met's record says hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649). **C**
- Concealed shoes: Shawcross says the reason why people concealed shoes remains a mystery; University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items, and that they were connected to notions of good luck and hope (S650). **C**
- Concealed shoes: Shawcross says the reason why people concealed shoes remains a mystery; University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items, and that they were connected to notions of good luck and hope (S650). **C**
```

For (c), the copied adjacent base propositions were S603 → S648, S612 → S651, S630 → S649, and S621 → S650. For (d2), both identical occurrences are shown above; the original four lines were retained and one duplicate was inserted beside each.

## Required one-line receipts

`counter-sha256` below identifies the frozen run; `probe-counter-sha256` identifies the independently scored probe. `exit` is frozen exit; `probe-exit` is probe exit. `stopped-by` lists all failing legs, not a short-circuit location (the counter prints every leg). Baseline and all restorations are included so no failed baseline is misrepresented as a killed mutant.

```text
RECEIPT CtlGenericA3/baseline counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/a-generic counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:ROWS,SUPPORT;probe:ROWS probe-exit=1 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/a-generic-restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/b-quote counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/b-quote-restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/c-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:LINES,ROWS,SUPPORT;probe:LINES,ROWS probe-exit=1 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/c-base-line-restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/d-same-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/d-same-line-restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/d-two-lines counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:LINES,SUPPORT;probe:LINES probe-exit=1 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
RECEIPT CtlGenericA3/d-two-lines-restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0 probe-counter-sha256=0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c
```

## Restoration evidence and hashes

The candidate entry before every mutation was `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`. Each mutant's exact entry bytes are archived at `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/<variant>-mutated-entry.md`. Each restoration compared all 84 baseline fixture-file hashes, including the entry, SOURCES, frozen counter, manifest/captures, packet/key/report/transcript bytes, and the key hash, and found exact equality. The restoration reports contain full per-file before/after mappings; no git reset/checkout was used to restore these mutations.

| Case | Entry sha256 while mutated | Entry sha256 after exact restoration | Compared fixture files |
|---|---|---|---|
| a-generic | `c2b106dba01fb90a82e9d37a4d58decf0438b0babee88982996f604ba85d6bfd` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` | 84; all equal |
| b-quote | `e039d91939cddc186b90fcbbdecf419850cd81c3258674c324793cec10eb134a` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` | 84; all equal |
| c-base-line | `983c3a118ce59a2ead99a89fe59cd6243330635f53bb83ead9cd3c5e1c44c145` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` | 84; all equal |
| d-same-line | `c254879b2eb569604e8fab647cfd2229641bf778f6b5995242d4a758849bbd21` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` | 84; all equal |
| d-two-lines | `3f2d1cb02eab0dcec3692bfa41460ef6074cc98c34e7e1ed175d5fc4a0354e1c` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` | 84; all equal |

Unchanged SOURCES sha256: `53b5a5f293cdf4199e7db1b8fc42d37bea4b4d830e1d9c375c50dcfad2028fca`.

| Unchanged capture artifact | Before/after sha256 |
|---|---|
| reports/round-60/captures/manifest.json | `49d98b8360af88f13c989afcfe306c28e0f4dace2e26b64b19aad3507f2ed745` |
| reports/round-60/captures/S648.bin | `2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a` |
| reports/round-60/captures/S649.bin | `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` |
| reports/round-60/captures/S650.bin | `5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5` |
| reports/round-60/captures/S651.bin | `8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79` |

Recorded restoration messages (the restored entry and all fixture hashes were checked before each restored detector run):

```text
RESTORED a-generic entry=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 all_84_tracked_fixture_hashes_equal
RESTORED b-quote entry=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 all_84_tracked_fixture_hashes_equal
RESTORED c-base-line entry=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 all_84_tracked_fixture_hashes_equal
RESTORED d-same-line entry=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 all_84_tracked_fixture_hashes_equal
RESTORED d-two-lines entry=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 all_84_tracked_fixture_hashes_equal
```

Restoration artifacts: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/outputs/<variant>-restoration.json`. Scored state hashes: `outputs/<variant>-state.json`; full scored synthetic support snapshots: `evidence-<variant>/`. Final clone state is the exact inherited candidate plus its restored baseline fixture, not any mutant.

## Full detector stdout and exits (22 runs)

These blocks paste the recorded subprocess stdout without line truncation or omissions. Every run had empty stderr. The files `outputs/<label>-score.json` also retain the exact command, cwd, complete stdout/stderr, exit, and executed-counter sha256.

### baseline / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### baseline / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### a-generic / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-0-quote-words', 'S649:line-shares-1-quote-words', 'S650:line-shares-0-quote-words', 'S651:line-shares-0-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-generic / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-0-quote-words', 'S649:line-shares-1-quote-words', 'S650:line-shares-0-quote-words', 'S651:line-shares-0-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### a-generic-restored / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-generic-restored / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### b-quote / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-quote / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### b-quote-restored / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-quote-restored / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### c-base-line / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True', 'S649:lines=1 base_line=True', 'S650:lines=1 base_line=True', 'S651:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words', 'S649:line-shares-0-quote-words', 'S650:line-shares-0-quote-words', 'S651:line-shares-1-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-base-line / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True', 'S649:lines=1 base_line=True', 'S650:lines=1 base_line=True', 'S651:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words', 'S649:line-shares-0-quote-words', 'S650:line-shares-0-quote-words', 'S651:line-shares-1-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### c-base-line-restored / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-base-line-restored / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### d-same-line / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### d-same-line / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### d-same-line-restored / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### d-same-line-restored / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### d-two-lines / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=2 base_line=False', 'S649:lines=2 base_line=False', 'S650:lines=2 base_line=False', 'S651:lines=2 base_line=False']
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### d-two-lines / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=2 base_line=False', 'S649:lines=2 base_line=False', 'S650:lines=2 base_line=False', 'S651:lines=2 base_line=False']
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### d-two-lines-restored / frozen

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B reports/round-60/accept-d.py`. Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### d-two-lines-restored / probe

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/accept-d-probe.py`. Counter sha256: `0546f553421b871cdcbf719c388e6fee7cea0f78c7ca0f6a334088c19236f09c`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

## Full fixture-builder stdout and exits (6 runs)

### baseline packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

### a-generic packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

### b-quote packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

### c-base-line packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

### d-same-line packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

### d-two-lines packet build

Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone`. Command: `timeout --kill-after=5 30 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlGenericA3/clone/.ufo/waves/round-60/support`.

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

## Tooling, bounds, and ownership

- Environment addition: **pypdf 5.4.0**, official PyPI package via `uv run --no-project --quiet --with pypdf==5.4.0`, needed by the frozen locator to extract the pinned S648 PDF. Its isolated setup run printed `pypdf=5.4.0` and exited 0. No global install/update or pacman transaction occurred.
- No external page fetches were made by this control; captures came from the assigned L1 artifacts. Synthetic page-read calls are fixture strings, not executed reads.
- Every shell/process command had a deadline <=600 seconds; detectors had 120-second process-group deadlines with 5-second kill grace. All completed synchronously; no background job, service, subagent, or other agent runtime was started.
- Sandbox size measured after the final restoration: **151272463 bytes**, below 200 MB. No append-loop logs or imported-file markers.
- No lane, sibling, fleet, or real session file was modified; the sole lane write is this scoped report. All clone operations, mutations, packets, fake sessions, logs, and dependency caches are under the assigned scratch directory.
- The 30-minute assignment was completed without extending into the later support/data wave.

The assigned mutation/control probe is complete. No contract, source-row, candidate-build, or production-counter change is proposed or shipped by this seat.
