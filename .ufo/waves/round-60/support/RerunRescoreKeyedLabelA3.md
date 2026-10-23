HOLDS

# RerunRescoreKeyedLabelA3 — independent re-measure of pre-data control receipts under the FROZEN counter

Scope: falsify the wave-1/L1 report `kotodama-shokunin/.ufo/waves/round-60/resid-a3/RescoreKeyedLabelA3.md` (revision-7 packet-only shortcut re-score). Re-run its fixtures with its own commands against the FROZEN counter declared at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (claims.json `freeze_note`). All work was done read-only in the lane, sandbox-only under `/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreKeyedLabelA3/`, with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B` for every python run, every process capped with `timeout`, and no git/jj write anywhere. No tool install was needed or performed (uv cache reused offline). No live network fetch was performed.

## 1. Frozen counter identity (the receipts named an earlier counter sha256 — confirmed)

The reference receipts name `counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59` at `rev=1cd9db7cdc83fd41f5d04cd620af879555442f19`. This is the revision-8 counter. The frozen declaration at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` pins revision 9 (`cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d`), and the frozen counter file at the freeze commit is byte-identical to the revision-9 introduction (a56b04fc). Every fixture below was therefore re-scored under revision 9.

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ for c in 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 a56b04fc 1cd9db7c 14e64138 b60e6d4e; do printf '%s ' "$c"; git show "$c:reports/round-60/accept-d.py" | sha256sum; done
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d  -
a56b04fc cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d  -
1cd9db7c 45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59  -
14e64138 b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc  -
b60e6d4e 43a90494a231fda0edb5e3b9bbec5fe2e81d2caac9314a847fecfb2d8d3b296b  -
$ diff <(git show 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626:reports/round-60/accept-d.py) <(git show a56b04fc:reports/round-60/accept-d.py) && echo IDENTICAL-FROZEN-REV9
IDENTICAL-FROZEN-REV9
```

Adaptation required by revision 9 relative to the receipts' revision 8: only the counter executable itself (revision 9 = revision 8 + the CONFINE_DENY `\/` token per `revision_note_9`; EVIDENCE unchanged). No fixture needed any behavior change; the only fixture adaptions are path plumbing (below).

## 2. Independent setup (fresh clone at the frozen commit, copied reference scripts)

```
$ MY=/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreKeyedLabelA3
$ git clone --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin $MY/clone
Cloning into '/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreKeyedLabelA3/clone'...
done.
$ git -C $MY/clone rev-parse HEAD
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
$ sha256sum $MY/clone/reports/round-60/accept-d.py $MY/clone/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d  .../clone/reports/round-60/accept-d.py
36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2  .../clone/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
$ cp -a /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/inherited-support/. $MY/inherited-support/
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/guess.py $MY/
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/predictions.json $MY/
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/r9/packet-only-repeated-word.py $MY/r9/
$ cp -a /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/uv-cache $MY/uv-cache
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/r9/fixtures.py $MY/r9/fixtures.py
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/r9/score.py $MY/r9/score.py
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/fixtures.py $MY/legacy-fixtures.py
$ cp /fast/scratch/hyaku/kotodama-r60a3/RescoreKeyedLabelA3/score.py $MY/legacy-score.py
```

Named adaptations (each limited to what the frozen counter / the independent sandbox requires; nothing else changed):

1. `r9/fixtures.py`, `r9/score.py`, `legacy-fixtures.py`: only the `BASE = Path(...)` line points at this sandbox (the original hardcodes the reference sandbox). All case lists, assertions, probes, and statistics code are untouched.
2. `legacy-score.py` (the reference top-level runner, which asserted the revision-8 hash `45ce3ef...`): BASE path; probe filename `accept-d-probe-legacy.py`; the frozen-hash assertion updated to `cf068177...` (revision 9); the probe audit block updated from the revision-8 API (`EVIDENCE_SPAN` regex) to the revision-9 API (`QUOTE_CHARS` quote-pair parsing + `norm_forms` norms), mirroring `r9/score.py`'s audit verbatim.
3. `make-legacy-probe.py` (new helper, modeled on the reference `prepare-rescore.py` probe step): derives `accept-d-probe-legacy.py` from the frozen source by substituting **only** the `SESSIONS` constant, and writes `probe-legacy.diff`.
4. The r9 probe (`r9/accept-d-probe.py`) and diff are produced by `r9/fixtures.py` itself (unchanged logic), substituting only `SESSIONS`.

Both probe diffs are exactly the SESSIONS line and nothing else:

```
$ cat r9/probe.diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -263,7 +263,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreKeyedLabelA3/r9/fake-sessions/{seat}.jsonl"  # synthetic control fixture
 
 
 def tool_calls(transcript):
$ cat probe-legacy.diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -263,7 +263,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreKeyedLabelA3/fake-sessions/{seat}.jsonl"  # synthetic control fixture
 
 
 def tool_calls(transcript):
```

```
$ PYTHONDONTWRITEBYTECODE=1 python3 -B make-legacy-probe.py
probe_sha256=8e38d6bb19a7e2d6565a34ccb839574468539cdf4ef971f75a6b9af3994192bd
```

## 3. Fixture generation (the reference commands, re-run)

Each case regenerates packets/reports/transcripts/registry/key from the inherited CtlKeyedLabelA3 dry-run material into the clone's ` .ufo/waves/round-60/support` and the case dir; page text enters only the honest generator. Full fixture stats:

```
$ PYTHONDONTWRITEBYTECODE=1 python3 -B r9/fixtures.py as-written
{ "case": "as-written", "reports_byte_identical_to_inherited": 24, "planted_not": 48, "real_supported": 141, "supported_quoted": 0, "synthetic_curl_calls": 186, "changed_real_blocks": 42, "entry_sha256": "36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2", "classifier_invocations": 24, "repeated_generator_invocations": 0 }
$ PYTHONDONTWRITEBYTECODE=1 python3 -B r9/fixtures.py packet-quotes
{ "case": "packet-quotes", "reports_byte_identical_to_inherited": 0, "planted_not": 48, "real_supported": 141, "supported_quoted": 141, "synthetic_curl_calls": 186, "changed_real_blocks": 42, "entry_sha256": "36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2", "classifier_invocations": 24, "repeated_generator_invocations": 0 }
$ PYTHONDONTWRITEBYTECODE=1 python3 -B r9/fixtures.py repeated-word
{ "case": "repeated-word", "reports_byte_identical_to_inherited": 0, "planted_not": 48, "real_supported": 141, "supported_quoted": 141, "synthetic_curl_calls": 186, "changed_real_blocks": 42, "entry_sha256": "36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2", "classifier_invocations": 24, "repeated_generator_invocations": 24 }
$ PYTHONDONTWRITEBYTECODE=1 python3 -B r9/fixtures.py honest-shaped
{ "case": "honest-shaped", "reports_byte_identical_to_inherited": 0, "planted_not": 48, "real_supported": 141, "supported_quoted": 141, "synthetic_curl_calls": 186, "changed_real_blocks": 42, "entry_sha256": "36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2", "classifier_invocations": 24, "repeated_generator_invocations": 0 }
$ PYTHONDONTWRITEBYTECODE=1 python3 -B legacy-fixtures.py legacy-as-written
{ "case": "legacy-as-written", "reports_byte_identical_to_inherited": 24, "planted_not": 48, "real_supported": 141, "supported_quoted": 0, "synthetic_curl_calls": 186, "changed_real_blocks": 0, "entry_sha256": "36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2", "fixture_key_entry_sha256": "0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0" }
```

Inherited material pre-checks: `planted-rows.md` sha256 = `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682` = the frozen `PLANTED_ROWS_SHA256`; registry has exactly 24 frozen members (role reviewer, agentId `KotodamaR60A3.<name>`); inherited key entry_sha256 = `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` (the stale key the legacy fixture deliberately keeps).

## 4. Counter runs (frozen = revision 9 accept-d.py in the clone; probe = SESSIONS-only substitution)

Command per run: `timeout 600 python3 -B reports/round-60/accept-d.py` (frozen, cwd clone) / `timeout 600 python3 -B <probe>` (probe, cwd clone), env `PYTHONDONTWRITEBYTECODE=1`, `TMPDIR`/`UV_CACHE_DIR` sandbox-local, `UV_PYTHON_DOWNLOADS=never`, `UV_OFFLINE=1`. Full stdout and exit for every run follow (each run's stdout is complete; the SUPPORT line is given in full).

### 4.1 legacy-as-written / frozen (JUDGED fails first; SUPPORT fails; seats missing because key_ok is false)

```
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

### 4.2 legacy-as-written / probe

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=36bd628b6af6
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
exit=1
AUDIT {"any_quote_locates_in_other_page": 0, "any_quote_locates_in_packet": 0, "any_quote_locates_in_page": 0, "blind_failures": [], "bound_failures": [], "confined_failures": [], "evidenced": 0, "fetched": 141, "novel_ge5": 0, "novel_min": null, "quoted_ge10": 0, "quoted_lines": 0, "session_copy_failures": [], "supported_lines": 141}
```

### 4.3 as-written / frozen

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S636:NOT/SupportA60', 'S628:NOT/SupportA60', 'S627:NOT/SupportC60', 'S600:NOT/SupportE60', 'S617:NOT/SupportF60', 'S634:NOT/SupportF60', 'S630:NOT/SupportG60', 'S630:NOT/SupportH60', 'S638:NOT/SupportH60', 'S607:NOT/SupportL60', 'S650:NOT/SupportL60', 'S645:NOT/SupportM60', 'S619:NOT/SupportM60', 'S636:NOT/SupportM60', 'S631:NOT/SupportN60', 'S604:NOT/SupportN60', 'S638:NOT/SupportO60', 'S626:NOT/SupportQ60', 'S629:NOT/SupportS60', 'S620:NOT/SupportS60', 'S637:NOT/SupportS60', 'S625:NOT/SupportT60', 'S633:NOT/SupportT60', 'S617:NOT/SupportV60', 'S634:NOT/SupportV60', 'S609:NOT/SupportW60', 'S635:NOT/SupportW60', 'S644:NOT/SupportW60', 'S618:NOT/SupportW60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:transcript-not-session-copy', 'SupportB60:X2/sees:transcript-not-session-copy', 'SupportC60:X2/sees:transcript-not-session-copy', 'SupportD60:X2/sees:transcript-not-session-copy', 'SupportE60:X2/sees:transcript-not-session-copy', 'SupportF60:X2/sees:transcript-not-session-copy', 'SupportG60:X2/sees:transcript-not-session-copy', 'SupportH60:X2/sees:transcript-not-session-copy', 'SupportI60:X2/sees:transcript-not-session-copy', 'SupportJ60:X2/sees:transcript-not-session-copy', 'SupportK60:X2/sees:transcript-not-session-copy', 'SupportL60:X2/sees:transcript-not-session-copy', 'SupportM60:X2/sees:transcript-not-session-copy', 'SupportN60:X2/sees:transcript-not-session-copy', 'SupportO60:X2/sees:transcript-not-session-copy', 'SupportP60:X2/sees:transcript-not-session-copy', 'SupportQ60:X2/sees:transcript-not-session-copy', 'SupportR60:X2/sees:transcript-not-session-copy', 'SupportS60:X2/sees:transcript-not-session-copy', 'SupportT60:X2/sees:transcript-not-session-copy', 'SupportU60:X2/sees:transcript-not-session-copy', 'SupportV60:X2/sees:transcript-not-session-copy', 'SupportW60:X2/sees:transcript-not-session-copy', 'SupportX60:X2/sees:transcript-not-session-copy']
ACCEPT-D-60: FAIL
exit=1
```

### 4.4 as-written / probe

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
AUDIT {"any_quote_locates_in_other_page": 0, "any_quote_locates_in_packet": 0, "any_quote_locates_in_page": 0, "blind_failures": [], "bound_failures": [], "confined_failures": [], "evidenced": 0, "fetched": 141, "novel_ge5": 0, "novel_min": null, "quoted_ge10": 0, "quoted_lines": 0, "session_copy_failures": [], "supported_lines": 141}
```

### 4.5 packet-quotes / frozen

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S636:NOT/SupportA60', 'S628:NOT/SupportA60', 'S627:NOT/SupportC60', 'S600:NOT/SupportE60', 'S617:NOT/SupportF60', 'S634:NOT/SupportF60', 'S630:NOT/SupportG60', 'S630:NOT/SupportH60', 'S638:NOT/SupportH60', 'S601:NOT/SupportI60', 'S646:NOT/SupportI60', 'S620:NOT/SupportI60', 'S624:NOT/SupportJ60', 'S649:NOT/SupportJ60', 'S637:NOT/SupportK60', 'S611:NOT/SupportK60', 'S607:NOT/SupportL60', 'S650:NOT/SupportL60', 'S645:NOT/SupportM60', 'S619:NOT/SupportM60', 'S636:NOT/SupportM60', 'S631:NOT/SupportN60', 'S604:NOT/SupportN60', 'S638:NOT/SupportO60', 'S626:NOT/SupportQ60', 'S629:NOT/SupportS60', 'S620:NOT/SupportS60', 'S637:NOT/SupportS60', 'S625:NOT/SupportT60', 'S633:NOT/SupportT60', 'S617:NOT/SupportV60', 'S634:NOT/SupportV60', 'S609:NOT/SupportW60', 'S635:NOT/SupportW60', 'S644:NOT/SupportW60', 'S618:NOT/SupportW60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:transcript-not-session-copy', 'SupportB60:X2/sees:transcript-not-session-copy', 'SupportC60:X2/sees:transcript-not-session-copy', 'SupportD60:X2/sees:transcript-not-session-copy', 'SupportE60:X2/sees:transcript-not-session-copy', 'SupportF60:X2/sees:transcript-not-session-copy', 'SupportG60:X2/sees:transcript-not-session-copy', 'SupportH60:X2/sees:transcript-not-session-copy', 'SupportI60:X2/sees:transcript-not-session-copy', 'SupportJ60:X2/sees:transcript-not-session-copy', 'SupportK60:X2/sees:transcript-not-session-copy', 'SupportL60:X2/sees:transcript-not-session-copy', 'SupportM60:X2/sees:transcript-not-session-copy', 'SupportN60:X2/sees:transcript-not-session-copy', 'SupportO60:X2/sees:transcript-not-session-copy', 'SupportP60:X2/sees:transcript-not-session-copy', 'SupportQ60:X2/sees:transcript-not-session-copy', 'SupportR60:X2/sees:transcript-not-session-copy', 'SupportS60:X2/sees:transcript-not-session-copy', 'SupportT60:X2/sees:transcript-not-session-copy', 'SupportU60:X2/sees:transcript-not-session-copy', 'SupportV60:X2/sees:transcript-not-session-copy', 'SupportW60:X2/sees:transcript-not-session-copy', 'SupportX60:X2/sees:transcript-not-session-copy']
ACCEPT-D-60: FAIL
exit=1
```

### 4.6 packet-quotes / probe

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
AUDIT {"any_quote_locates_in_other_page": 0, "any_quote_locates_in_packet": 141, "any_quote_locates_in_page": 141, "blind_failures": [], "bound_failures": [], "confined_failures": [], "evidenced": 0, "fetched": 141, "novel_ge5": 0, "novel_min": 0, "quoted_ge10": 141, "quoted_lines": 141, "session_copy_failures": [], "supported_lines": 141}
```

### 4.7 repeated-word / frozen

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S636:NOT/SupportA60', 'S628:NOT/SupportA60', 'S627:NOT/SupportC60', 'S609:NOT/SupportD60', 'S644:NOT/SupportD60', 'S600:NOT/SupportE60', 'S617:NOT/SupportF60', 'S634:NOT/SupportF60', 'S630:NOT/SupportG60', 'S630:NOT/SupportH60', 'S638:NOT/SupportH60', 'S601:NOT/SupportI60', 'S646:NOT/SupportI60', 'S620:NOT/SupportI60', 'S624:NOT/SupportJ60', 'S649:NOT/SupportJ60', 'S637:NOT/SupportK60', 'S611:NOT/SupportK60', 'S607:NOT/SupportL60', 'S650:NOT/SupportL60', 'S645:NOT/SupportM60', 'S619:NOT/SupportM60', 'S636:NOT/SupportM60', 'S631:NOT/SupportN60', 'S604:NOT/SupportN60', 'S638:NOT/SupportO60', 'S626:NOT/SupportQ60', 'S629:NOT/SupportS60', 'S620:NOT/SupportS60', 'S637:NOT/SupportS60', 'S625:NOT/SupportT60', 'S633:NOT/SupportT60', 'S617:NOT/SupportV60', 'S634:NOT/SupportV60', 'S609:NOT/SupportW60', 'S635:NOT/SupportW60', 'S644:NOT/SupportW60', 'S618:NOT/SupportW60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:transcript-not-session-copy', 'SupportB60:X2/sees:transcript-not-session-copy', 'SupportC60:X2/sees:transcript-not-session-copy', 'SupportD60:X2/sees:transcript-not-session-copy', 'SupportE60:X2/sees:transcript-not-session-copy', 'SupportF60:X2/sees:transcript-not-session-copy', 'SupportG60:X2/sees:transcript-not-session-copy', 'SupportH60:X2/sees:transcript-not-session-copy', 'SupportI60:X2/sees:transcript-not-session-copy', 'SupportJ60:X2/sees:transcript-not-session-copy', 'SupportK60:X2/sees:transcript-not-session-copy', 'SupportL60:X2/sees:transcript-not-session-copy', 'SupportM60:X2/sees:transcript-not-session-copy', 'SupportN60:X2/sees:transcript-not-session-copy', 'SupportO60:X2/sees:transcript-not-session-copy', 'SupportP60:X2/sees:transcript-not-session-copy', 'SupportQ60:X2/sees:transcript-not-session-copy', 'SupportR60:X2/sees:transcript-not-session-copy', 'SupportS60:X2/sees:transcript-not-session-copy', 'SupportT60:X2/sees:transcript-not-session-copy', 'SupportU60:X2/sees:transcript-not-session-copy', 'SupportV60:X2/sees:transcript-not-session-copy', 'SupportW60:X2/sees:transcript-not-session-copy', 'SupportX60:X2/sees:transcript-not-session-copy']
ACCEPT-D-60: FAIL
exit=1
```

### 4.8 repeated-word / probe

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
AUDIT {"any_quote_locates_in_other_page": 0, "any_quote_locates_in_packet": 3, "any_quote_locates_in_page": 3, "blind_failures": [], "bound_failures": [], "confined_failures": [], "evidenced": 0, "fetched": 141, "novel_ge5": 0, "novel_min": 0, "quoted_ge10": 141, "quoted_lines": 141, "session_copy_failures": [], "supported_lines": 141}
```

### 4.9 honest-shaped / frozen

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S636:NOT/SupportA60', 'S628:NOT/SupportA60', 'S627:NOT/SupportC60', 'S609:NOT/SupportD60', 'S644:NOT/SupportD60', 'S600:NOT/SupportE60', 'S617:NOT/SupportF60', 'S634:NOT/SupportF60', 'S630:NOT/SupportG60', 'S630:NOT/SupportH60', 'S638:NOT/SupportH60', 'S601:NOT/SupportI60', 'S646:NOT/SupportI60', 'S620:NOT/SupportI60', 'S624:NOT/SupportJ60', 'S649:NOT/SupportJ60', 'S637:NOT/SupportK60', 'S611:NOT/SupportK60', 'S607:NOT/SupportL60', 'S650:NOT/SupportL60', 'S645:NOT/SupportM60', 'S619:NOT/SupportM60', 'S636:NOT/SupportM60', 'S631:NOT/SupportN60', 'S604:NOT/SupportN60', 'S638:NOT/SupportO60', 'S626:NOT/SupportQ60', 'S629:NOT/SupportS60', 'S620:NOT/SupportS60', 'S637:NOT/SupportS60', 'S625:NOT/SupportT60', 'S633:NOT/SupportT60', 'S617:NOT/SupportV60', 'S634:NOT/SupportV60', 'S609:NOT/SupportW60', 'S635:NOT/SupportW60', 'S644:NOT/SupportW60', 'S618:NOT/SupportW60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:transcript-not-session-copy', 'SupportB60:X2/sees:transcript-not-session-copy', 'SupportC60:X2/sees:transcript-not-session-copy', 'SupportD60:X2/sees:transcript-not-session-copy', 'SupportE60:X2/sees:transcript-not-session-copy', 'SupportF60:X2/sees:transcript-not-session-copy', 'SupportG60:X2/sees:transcript-not-session-copy', 'SupportH60:X2/sees:transcript-not-session-copy', 'SupportI60:X2/sees:transcript-not-session-copy', 'SupportJ60:X2/sees:transcript-not-session-copy', 'SupportK60:X2/sees:transcript-not-session-copy', 'SupportL60:X2/sees:transcript-not-session-copy', 'SupportM60:X2/sees:transcript-not-session-copy', 'SupportN60:X2/sees:transcript-not-session-copy', 'SupportO60:X2/sees:transcript-not-session-copy', 'SupportP60:X2/sees:transcript-not-session-copy', 'SupportQ60:X2/sees:transcript-not-session-copy', 'SupportR60:X2/sees:transcript-not-session-copy', 'SupportS60:X2/sees:transcript-not-session-copy', 'SupportT60:X2/sees:transcript-not-session-copy', 'SupportU60:X2/sees:transcript-not-session-copy', 'SupportV60:X2/sees:transcript-not-session-copy', 'SupportW60:X2/sees:transcript-not-session-copy', 'SupportX60:X2/sees:transcript-not-session-copy']
ACCEPT-D-60: FAIL
exit=1
```

### 4.10 honest-shaped / probe (the positive calibration PASSes)

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
AUDIT {"any_quote_locates_in_other_page": 0, "any_quote_locates_in_packet": 0, "any_quote_locates_in_page": 141, "blind_failures": [], "bound_failures": [], "confined_failures": [], "evidenced": 141, "fetched": 141, "novel_ge5": 141, "novel_min": 6, "quoted_ge10": 141, "quoted_lines": 141, "session_copy_failures": [], "supported_lines": 141}
```

(All ten runs were issued through the copied runners; each printed exactly the text above plus the `exit=` line and, for probes, the `AUDIT` JSON. Complete streams and receipt JSON are saved in `r9/cases/<case>/{frozen,probe}.{stdout,stderr,json}` and `cases/legacy-as-written/{frozen,probe}.{stdout,stderr,json}` in the sandbox.)

## 5. Receipt-by-receipt verdicts (reference receipt → my independent re-measure under the frozen revision-9 counter)

| Receipt (reference, revision-8 counter `45ce3ef...`) | Re-measure (frozen revision-9 counter `cf068177...`) | Outcome |
|---|---|---|
| `legacy-as-written` frozen=FAIL exit=1 probe=FAIL probe-exit=1 | frozen=FAIL exit=1 (JUDGED `entry_sha256 key=0073da7ed7e0 landed=36bd628b6af6`; SUPPORT FAIL 47×good=0; seats missing) · probe=FAIL probe-exit=1 (same) | **same outcome** |
| `as-written` frozen=FAIL exit=1 probe=FAIL probe-exit=1 | frozen=FAIL exit=1 (JUDGED PASS; SUPPORT FAIL; froze composition includes live-session NOT rejections, see §6) · probe=FAIL probe-exit=1 (47×good=0; evidenced=0) | **same outcome** |
| `packet-quotes` frozen=FAIL exit=1 probe=FAIL probe-exit=1 | frozen=FAIL exit=1 · probe=FAIL probe-exit=1 (141 quotes all in packet AND page, novel_ge5=0, evidenced=0) | **same outcome** |
| `honest-shaped` frozen=FAIL exit=1 probe=PASS probe-exit=0 | frozen=FAIL exit=1 · probe=PASS probe-exit=0 (evidenced=141, novel_ge5=141, none in packet, none in other page) | **same outcome** |

`repeated-word` is not in the reference receipt list (it is the revision-8 probe case); under the frozen counter it also FAILs on both modes (evidenced=0), consistent with `revision_note_8`'s requirement. No fixture that skips reading the pages reached PASS under either mode → **CONTROL-MET not observed**.

## 6. Findings by severity

**Medium — the frozen leg is not hermetic; its exact stream depends on live host sessions.** The frozen counter's dissent scan globs `/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl`. At re-measure time, 24 genuine session files for `SupportA60..SupportX60` exist there (session dir `2026-10-23T06-27-20-968Z_01a16771-...`, mtimes 04:52–04:54Z during this run). They inject real NOT-SUPPORTED verdicts (`S636:NOT/SupportA60`, `S628:NOT/SupportA60`, `S627:NOT/SupportC60`, `S600:NOT/SupportE60`, …) into the frozen output. The reference's own saved `as-written/frozen.stdout` has 0 such entries (verified directly against the reference sandbox's saved file); mine has 29. The receipt label (FAIL) and exit (1) are unchanged, so the receipt holds, but the exact frozen stdout is time-dependent and cannot be bit-reproduced. This is a property of the counter (its SESSIONS glob is by design), not of the fixtures.

**Low — the receipts' counter hash is an earlier revision.** The four receipts name `counter-sha256=45ce3ef...` (revision 8); the frozen declaration pins revision 9 (`cf068177...`). The difference is the revision-9 CONFINE_DENY `\/` token only; EVIDENCE semantics are identical, and every outcome reproduced.

**Low — `legacy-as-written` is not a probe-visible EVIDENCE case.** Because JUDGED fails first (stale key `0073da7...` vs landed `36bd628b...`), seats never qualify; the L1's receipt correctly labels this as a stale-identity failure, and my re-measure agrees. The fixture shape is exactly a literal replay (24/24 reports byte-identical, 0 blocks changed, old key kept, transcripts untouched).

## 7. Fixture-shape verification (does each fixture do what its label claims? yes, all five)

- `legacy-as-written`: literal replay of the inherited dry-run material — reports byte-identical to inherited (24/24), packet bytes untouched (changed_real_blocks=0), key left at `0073da7...`, transcripts untouched, no page reads. Accurate.
- `as-written`: preserves all 24 inherited report files byte-for-byte (24/24); refreshes the 42 real packet blocks from the committed SOURCES/entry fields (`changed_real_blocks=42`), updates the key to the measured entry sha `36bd628b...`, re-runs the packet-only classifier and asserts verdict identity with the inherited predictions (24 invocations, all asserts passed). It does **not** secretly do the review work: it never reads page text (`pages={}` in the generator), and its probe still fails EVIDENCE (evidenced=0). Accurate.
- `packet-quotes`: spans are taken only from packet fields (`quote`/`teaches`/`entry`), no page text is read; audit confirms all 141 quotes locate in the packet block (and, because the quote cells are page-derived, also in the page) with 0 novel distinct words, so EVIDENCE rejects them. Accurate.
- `repeated-word`: spans come from the packet-only repeated-word generator (24 invocations), no page text read; audit 0 evidenced. Accurate.
- `honest-shaped`: the only generator that receives pinned page text (`page_texts`); its spans are verified page-only (in page 141/141, in packet 0, in other pages 0, novel distinct ≥5 for 141/141, min novel 6) and it is the only probe PASS. Accurate.

## 8. Residual risks and verification gaps

- The frozen-mode dissent input (host sessions) is a moving target; the receipt labels hold regardless, but a strict byte-for-byte re-run of the frozen stdout is impossible while live support sessions exist.
- I did not re-verify the classifier's saved-rule claim (`hybrid_tail_0.2`) independently; I relied on the fixtures' own assertion that regenerated verdicts equal the inherited report verdicts/predictions (all assertions passed).
- The honest-shaped PASS is a calibration fixture about the counter's EVIDENCE predicate; it does not claim any live support seat or genuine session provenance (the fixture transcripts are synthetic), consistent with the reference report.

No counter correction is indicated by this re-measure: the frozen revision-9 counter rejects all packet-only shortcuts (including the revision-8 repeated-word shape) and passes the honest page-reading calibration.
