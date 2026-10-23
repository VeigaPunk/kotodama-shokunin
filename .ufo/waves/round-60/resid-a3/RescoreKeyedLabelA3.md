NONE-MET

# RescoreKeyedLabelA3 — revision-7 packet-only shortcut re-score

## Result / strongest counterexample

The requested two negative controls both **FAIL under the frozen counter and the SESSIONS-only probe**. The honest-shaped positive **PASSes the probe**, exit 0. No packet-only page-reading bypass was observed.

The strongest negative is `packet-quotes`: the unchanged packet-only classifier gets **48/48 planted occurrences NOT-SUPPORTED, 141/141 real occurrences SUPPORTED, and 24/24 exact seats** on both the inherited and pinned-build-adapted packets. Every one of its 141 SUPPORTED lines then quotes >=10 words copied from its own packet. **All 141 quotes also locate in their pinned source page**, and all 141 labels have fetch-shaped page calls. Nevertheless, all 141 fail EVIDENCE because the quotes locate in the packet block. Under the probe, all 24 seats qualify but every cited id has `good=0`. This isolates the revision-7 exclusion rather than merely failing provenance, classification, quote length, or page location.

`as-written` preserves all 24 inherited report files byte-for-byte, including their old entry-hash header and bare verdict lines. Its probe also has 24 qualified seats, 141 fetch-shaped real verdicts, and zero EVIDENCE spans. EVIDENCE is implemented inside SUPPORT, not printed as a separate counter leg.

The positive has 48 planted NOTs and 141 real SUPPORTED lines; all 141 quote >=10 locator-normalised words from the pinned page text, with none locating in that label's packet block. The probe counts them and returns PASS. Its 186 synthetic curl calls retain cwd `/tmp/<Seat>` and literal packet URLs. These calls are fixture data, **not executed network fetches**; no live support seat or genuine session provenance is claimed. The positive generator actually reads the pinned text files; the packet-only classifier does not receive those texts.

## Axes and smallest safe correction

- **Depth / evidence soundness:** distinguish exact labels and a source-locating packet quote from evidence of reading additional page text.
- **Calibration / provenance:** distinguish frozen rejection, probe rejection, and positive calibration; do not call a stale-key or synthetic-provenance failure an EVIDENCE kill.
- **Operability:** preserve the honest-shaped probe PASS while rejecting both shortcut forms.
- **Freshness / identity:** score the committed build rather than silently restoring its older candidate entry.

No counter correction is indicated by these assigned controls. Retain the revision-7 page-span-and-not-packet predicate. A fixable **fixture identity defect** was found and corrected only in the private fixture: the inherited dry-run key binds entry `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`, whereas the requested build contains entry `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`. The entries differ substantively, not just in metadata. A literal replay is therefore separately scored as `legacy-as-written`; its JUDGED failure is not evidence that revision 7 killed the shortcut.

For the three calibrated cases, the smallest fixture-only correction was to preserve the inherited seat/label assignment and all planted blocks, refresh real packet fields from the pinned build using the committed builder's formatting, update the fixture key/packet entry hash and dispatched-task packet bytes, and recompute the dry-run key declaration. This changes 42 real block occurrences; no label mapping is changed. Original reports remain byte-identical for `as-written`. No entry, SOURCES row, capture, planted row, frozen counter, canonical contract, axis, route, or judgment was changed. These observations do not establish saturation or authorize admission; no harmful tradeoff was observed in this positive calibration, and the canonical Rust judge remains the only judge.

## Pin, preparation, and reproducibility

- Scored clone checkout: `1cd9db7cdc83fd41f5d04cd620af879555442f19`.
- Frozen counter SHA-256: `45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59`.
- Probe SHA-256: `58fb38dc3a32e1abfeb069664c175c2c3b121556abee4b5ec09b3fa2f229a069`.
- Byte-copied `guess.py` SHA-256: `ad2db40f4f8f30f1729f0c3da9ee3593d68338595b7843d63cc132fcbb11fb17`.
- Original dry-run key SHA-256: `29c21446af82b09dec8391840a68045fa69797c068d3d2da7de1fa76823c86fd`.
- Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/`.

Read claims.json revision_note_6 and revision_note_7 first, then inspected and copied the supplied classifier and harness. The classifier is unchanged. `inherited/{guess,evaluate,fixture,detect}.py` and `inherited-support/` retain the original files. The copied `evaluate.py` changes only its BASE path to this sandbox and was run on both inherited and adapted packets. Its saved best rule remains `hybrid_tail_0.2`; the key is opened only after classifier invocations finish. `fixtures.py` materialises the four explicitly synthetic cases; `score.py` saves complete counter stdout, stderr, exit, command, and hash in each `cases/<case>/` directory. Each case also retains its reports, packets, transcripts, fake-session copies, stats, quoted spans, and helper-level audit. All eight stderr streams are empty.

The frozen subprocess command was `timeout 600 python3 -B reports/round-60/accept-d.py`, cwd the pinned clone. The probe uses the same cwd and invocation with its absolute script path. Both inherit `PYTHONDONTWRITEBYTECODE=1`, sandbox-local TMPDIR/UV_CACHE_DIR, `UV_PYTHON_DOWNLOADS=never`, and `UV_OFFLINE=1`. Runner and subprocess deadlines bound the whole call below 600 seconds. Independent frozen/probe reads ran concurrently; cases were sequenced because they share the disposable clone's fixture paths. No background job, delegation, live reviewer, or other model/judgment runtime was invoked.

### Entire permitted probe diff

```diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -235,7 +235,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/fake-sessions/{seat}.jsonl"  # synthetic control fixture
 
 
 def tool_calls(transcript):
```

## Receipts

```text
RECEIPT RescoreKeyedLabelA3/legacy-as-written counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreKeyedLabelA3/as-written counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT(PROVENANCE,EVIDENCE);probe:SUPPORT(EVIDENCE) probe-exit=1
RECEIPT RescoreKeyedLabelA3/packet-quotes counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT(PROVENANCE,EVIDENCE);probe:SUPPORT(EVIDENCE) probe-exit=1
RECEIPT RescoreKeyedLabelA3/honest-shaped counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT(PROVENANCE);probe:none probe-exit=0
```

### Helper-level evidence audit, after report creation

| Case | Real SUPPORTED | Fetch-shaped | Quoted >=10 words | Quote in page | Quote in packet | EVIDENCE true | Probe outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| legacy-as-written | 141 | 141 | 0 | 0 | 0 | 0 | FAIL: stale judged identity |
| as-written | 141 | 141 | 0 | 0 | 0 | 0 | FAIL: EVIDENCE |
| packet-quotes | 141 | 141 | 141 | 141 | 141 | 0 | FAIL: EVIDENCE |
| honest-shaped | 141 | 141 | 141 | 141 | 0 | 141 | PASS |

Every case's probe-helper audit has empty blind, confined, bound, and session-copy failure lists. In the literal legacy case, JUDGED fails first and the counter does not qualify the seats; the empty helper lists are not qualification claims.

For example, the packet quote for SupportA60/P01 is `The amulet is an object with natural magical properties, whereas a talisman must be charged with magical powers by a creator` (21 normalised words). It locates in both the page and packet, so is rejected. The positive quotes additional surrounding text from that page: `and misfortune during his life on earth. There were good spirits as well with protective virtues. The amulet is an object with natural magical` (24 words), which does not locate in the block. Full per-verdict spans are in each case's `quotes.json`.

## Full stdout and exits

### legacy-as-written / frozen

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=36bd628b6af6
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
exit=1
```

### legacy-as-written / probe

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=36bd628b6af6
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
exit=1
```

### as-written / frozen

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

### as-written / probe

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### packet-quotes / frozen

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

### packet-quotes / probe

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### honest-shaped / frozen

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

### honest-shaped / probe

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

## Bounds and tooling

`timeout 20 du -sb <sandbox>` reported 161,910,268 bytes; `timeout 20 du -s -B1 <sandbox>` reported 190,992,384 allocated bytes, both below 200 MB. The later report write is outside that sandbox and is bounded to this report. Fixture writers enforce per-file limits; counter streams and receipt JSON are explicitly bounded. The clone was created with the assigned no-hardlinks command and checked out at the assigned commit; no lane or fleet git write was run. Originals were never edited, and nothing was written under `/home/vgpnk/.omp/`.

No tool installation or update was performed. The existing official pypdf 5.4.0 uv cache was copied into this sandbox for the counter's declared PDF parser, with offline operation enabled. A preparation-only assertion initially followed interpreter symlinks while estimating cache size; it stopped before copying the cache. Only that unfinished preparation step was resumed with symlink-aware sizing. No counter run failed for that preparation issue. The tool reported pty unavailability on the first pair; both runs completed synchronously in approximately 1.4 seconds, and later runs explicitly used no pty.

This is the completed assigned control review, not an admission, integration, source change, or claim of genuine support-seat work.
