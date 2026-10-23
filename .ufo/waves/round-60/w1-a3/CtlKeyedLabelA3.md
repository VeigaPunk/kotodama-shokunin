CONTROL-MET: packet-feature-hybrid (SESSIONS-only probe)

# CtlKeyedLabelA3 — packet-only keyed-shortcut control

## Result and scope

The best packet-only rule marked **all 48 planted occurrences NOT-SUPPORTED and all 141 real occurrences SUPPORTED**, across **all 24 dry-run packets**. These are 16 distinct planted blocks and 47 distinct real blocks, each repeated three times, not 189 independent propositions. The exact-seat result is **24/24**. The SESSIONS-only probe returned **ACCEPT-D-60: PASS, exit 0**. The unmodified frozen counter returned **FAIL, exit 1**, solely at SUPPORT because the synthetic transcripts have no authentic session files. No genuine provenance bypass was demonstrated.

**Mutation verdict:** SURVIVED in the explicitly permitted SESSIONS-only probe; INCONCLUSIVE as a mutation-kill test against the frozen counter, whose pristine baseline also fails provenance. This is a coverage finding about packet-feature discrimination and semantic work, not an endorsement of the entry or an integration decision.

All reports, transcripts and curl-call records in this experiment are explicitly synthetic fixtures. No live data reviewer was dispatched, messaged, or used. The curl records are **included but not executed**: the classifier never receives a page response. The only page bytes processed by the counter are its pinned local captures. Thus the probe result does not claim observed network fetches. The role of the synthetic calls is to exercise FETCHED/CONFINED after the allowed SESSIONS substitution, not to manufacture real review evidence.

## Axes

1. Planted recall (higher is better).
2. Real false-NOT rate (lower is better; any real NOT kills the counter).
3. Exact classification across all 24 seats and two-seat real-id coverage.
4. Frozen/probe acceptance, distinguished rather than conflated.
5. Byte-exact restoration and bounded scratch use.

## Provenance and preparation

Read the declaration first. Checked out `14e6413820d482913f723432b62d566967ccd1a6` in a private `git clone --no-hardlinks`, then applied the inherited L1 `build.patch` only there. Copied L1 captures and the held-out planted file into the private clone. No source, packet, key, capture or counter in the lane was changed. The only lane write is this report.

Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlKeyedLabelA3/`.

The packet builder was run once, with its original random seed generation, from the patched clone:

```text
python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/CtlKeyedLabelA3/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/CtlKeyedLabelA3/clone/.ufo/waves/round-60/support
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

Hashes:

- Frozen counter: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.
- SESSIONS-only probe: `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5`.
- Candidate entry: `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`.
- Planted rows: `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682` (matches the counter's pinned value).
- Dry-run packet key: `29c21446af82b09dec8391840a68045fa69797c068d3d2da7de1fa76823c86fd`.
- Packet-only program: `ad2db40f4f8f30f1729f0c3da9ee3593d68338595b7843d63cc132fcbb11fb17` (`guess.py`).
- Per-packet hashes: `preparation.json` in the sandbox; all detector-input hashes: `pristine-state.json`, `mutated-state.json`, `restored-state.json`.

A first preparation invocation failed before packet generation because captures were not a committed directory at the frozen revision. Created that directory in the sandbox, then successfully ran the builder above. No packet set from a failed build was scored.

## Packet-only program and evaluation

`guess.py` consumes **one packet through stdin** and emits feature verdicts. It imports only the standard library and has no explicit file or network read, key access, registry access, lane path access, cross-packet state, or source-page lookup. `evaluate.py` ran these 24 independent invocations with at most eight concurrent short-lived children, saved all predictions, and only then opened the key in the evaluation harness to score them. The fixture's packet mode re-ran the program, rather than substituting keyed verdicts.

Important limitation: this is **exploratory, in-sample feature engineering**, not a held-out estimate of a scholarly verifier. The analyst read the supplied planted-file structure and instruments while constructing the experiment, and the grammar/collocation cues are seed-specific. The program itself still receives only packet text; there is no label lookup or key membership in its decision. No inference is made about unseen planted families or a later packet population.

Best rule: `hybrid_tail_0.2`. It emits NOT-SUPPORTED if **any** of these packet-visible conditions holds:

1. A semicolon introduces an ungraded trailing clause after an empty citation or a bold tier: `(?:\*\*[A-C]\*\*|\(\s*\))\s*;[^*]*\.\s*$` on entry text.
2. The quote matches one of the six lexical/grammar anomaly patterns in `odd_quote` below.
3. The quote's content-word coverage in `(teaches + entry)` is below `0.2`.

Content words are NFKC/casefolded ASCII letter sequences of length at least four minus the program's stopword set. Coverage is `len(quote_words & other_words) / len(quote_words)`; an empty quote has coverage zero. This is lexical matching, not source support.

The best hybrid consists of disjoint successful cues here: quote anomalies recover 18/48 occurrences (six altered quotes), low quote-versus-(teaches+entry) overlap recovers 15/48 (five cross-wires), and the trailing-clause structure recovers 15/48 (five invented clauses), each with zero real false-NOTs. Real blocks receive three counted synthetic SUPPORTED verdicts each in the probe.

The first hybrid caught 45/48 planted occurrences with 0/141 false-NOTs and 21/24 exact seats. Broadening the tier-only suffix cue to an ungraded suffix after a citation recovered the remaining three repetitions of one planted block: recall improved to 48/48, false-NOTs stayed zero, exact seats improved to 24/24. This was retained as a Pareto improvement. No new packet seed was selected to improve the result.

### Complete program

```python
#!/usr/bin/env python3
"""Packet-only classifier: stdin packet -> JSON verdicts. No file/network reads.

Rules use only the text of this one packet, not a key, row registry, source page,
other packet, or persistent state. Exploratory lexical/grammar cues are explicitly
seed-specific and are not a claim of generalisation to later blind packets.
"""
import json
import re
import sys
import unicodedata
from urllib.parse import urlsplit

BLOCK = re.compile(r'^### (P\d{2})\n((?:(?!### ).*\n?)*)', re.M)
FIELD = re.compile(r'^(url|quote|teaches|entry):[ \t]*(.*)$', re.M)
STOP = set('about above after again against also among because been before being between both could does doing during each from further have having into itself just more most only other over same should some such than that their theirs them then there these they this those through under until very were what when where which while whom will with would your'.split())


def words(text):
    norm = unicodedata.normalize('NFKC', text).casefold()
    return {w for w in re.findall(r'[a-z]{4,}', norm) if w not in STOP}


def coverage(a, b):
    a, b = words(a), words(b)
    return len(a & b) / len(a) if a else 0.0


def blocks(text):
    return [(label, dict(FIELD.findall(body)), body) for label, body in BLOCK.findall(text)]


def odd_quote(text):
    text = text.strip().strip('"')
    cues = (
        r'\b(?:evil|holy|magical|unusual)\s+(?:whereas|firstly|although|therefore)\b',
        r'\bin\s+(?:consists|contains|has|is|was)\s+to\b',
        r'\b(?:with|of|by|from)\s+(?:firstly|secondly|therefore|whereas)\b',
        r'\bthis\s+\w+(?:ous|ive|al|ic)\s+(?:was|is)\b',
        r'\bmaterials,\s+\w+ing\s+to\s+(?:make|protect|ward|avert)\b',
        r'^(?:folklore|religion|archaeology|history|mythology|anthropology)\s+(?:amulet|talisman|charm)\s+holders\b',
    )
    return any(re.search(p, text, re.I) for p in cues)


def classify(text):
    packet = blocks(text)
    labels = [label for label, _, _ in packet]
    sizes = sorted(packet, key=lambda item: (len(item[2]), item[0]))
    short = {label for label, _, _ in sizes[:2]}
    long = {label for label, _, _ in sizes[-2:]}
    out = {}
    for label, f, body in packet:
        quote, teaches, entry = (f.get(name, '') for name in ('quote', 'teaches', 'entry'))
        qe = coverage(quote, entry)
        qt = coverage(quote, teaches)
        qboth = coverage(quote, teaches + ' ' + entry)
        et = coverage(entry, teaches)
        title_tail = bool(re.search(r'\*\*[A-C]\*\*\s*;', entry))
        ungraded_tail = bool(re.search(r'(?:\*\*[A-C]\*\*|\(\s*\))\s*;[^*]*\.\s*$', entry))
        place_date = bool(re.search(r'\b(?:\d{3,4}|\w+(?:th|st|nd|rd)-century|dynasty|Norway|Angkor|Edinburgh|Nanjing|Lima)\b', entry, re.I))
        odd = odd_quote(quote)
        values = {
            'all_supported': False,
            'all_not_supported': True,
            'first_two': label in labels[:2],
            'last_two': label in labels[-2:],
            'label_odd': int(label[1:]) % 2 == 1,
            'shortest_two': label in short,
            'longest_two': label in long,
            'place_or_date': place_date,
            'post_tier_semicolon': title_tail,
            'ungraded_citation_tail': ungraded_tail,
            'odd_quote_grammar': odd,
        }
        for name, value in (('quote_entry', qe), ('quote_teaches', qt), ('quote_both', qboth), ('entry_teaches', et)):
            for threshold in (0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7):
                values[f'{name}_lt_{threshold:g}'] = value < threshold
        for threshold in (0.1, 0.2, 0.25, 0.3, 0.35, 0.4):
            values[f'hybrid_{threshold:g}'] = title_tail or odd or qboth < threshold
            values[f'hybrid_tail_{threshold:g}'] = ungraded_tail or odd or qboth < threshold
        urls = re.findall(r'https?://\S+', f.get('url', ''))
        host = urlsplit(urls[0]).netloc.lower().removeprefix('www.') if urls else ''
        values['first_host=' + host] = True
        out[label] = {
            'features': {'chars': len(body), 'host': host, 'quote_entry': qe,
                         'quote_teaches': qt, 'quote_both': qboth,
                         'entry_teaches': et, 'post_tier_semicolon': title_tail,
                         'odd_quote_grammar': odd, 'place_or_date': place_date,
                         'ungraded_citation_tail': ungraded_tail},
            'rules': {name: ('NOT-SUPPORTED' if bad else 'SUPPORTED') for name, bad in values.items()},
        }
    hosts = {x['features']['host'] for x in out.values()}
    for result in out.values():
        for host in hosts:
            result['rules'].setdefault('first_host=' + host, 'SUPPORTED')
    return out


if __name__ == '__main__':
    text = sys.stdin.read(128 * 1024 + 1)
    if len(text) > 128 * 1024:
        raise SystemExit('packet exceeds 128 KiB bound')
    print(json.dumps(classify(text), sort_keys=True))
```

### Per-feature results

Each listed rule emits NOT-SUPPORTED when its predicate fires. A host rule matches the first URL host; first/last-two are packet block positions (also lowest/highest labels in these packets); shortest/longest-two rank the raw block character length. The table includes all evaluated overlap thresholds, each observed host, simple controls, and hybrid variants. Recall and false-NOT denominators count repeated packet occurrences; exact seats require every planted block rejected and no real block rejected.

| Rule | Planted recalled / 48 | Real false-NOT / 141 | Exact seats / 24 |
|---|---:|---:|---:|
| `all_not_supported` | 48/48 (100.00%) | 141/141 (100.00%) | 0/24 |
| `all_supported` | 0/48 (0.00%) | 0/141 (0.00%) | 0/24 |
| `entry_teaches_lt_0.1` | 0/48 (0.00%) | 0/141 (0.00%) | 0/24 |
| `entry_teaches_lt_0.2` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `entry_teaches_lt_0.25` | 0/48 (0.00%) | 12/141 (8.51%) | 0/24 |
| `entry_teaches_lt_0.3` | 3/48 (6.25%) | 18/141 (12.77%) | 0/24 |
| `entry_teaches_lt_0.35` | 9/48 (18.75%) | 30/141 (21.28%) | 0/24 |
| `entry_teaches_lt_0.4` | 15/48 (31.25%) | 48/141 (34.04%) | 0/24 |
| `entry_teaches_lt_0.5` | 24/48 (50.00%) | 69/141 (48.94%) | 0/24 |
| `entry_teaches_lt_0.6` | 36/48 (75.00%) | 96/141 (68.09%) | 0/24 |
| `entry_teaches_lt_0.7` | 45/48 (93.75%) | 111/141 (78.72%) | 0/24 |
| `first_host=agecrofthall.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=api.vam.ac.uk` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=archaeopress.com` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=archive.org` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=asianethnology.scholasticahq.com` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=aub.edu.lb` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=booksalongthesilkroads.library.utoronto.ca` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=cam.ac.uk` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=clevelandart.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=collections.vam.ac.uk` | 3/48 (6.25%) | 9/141 (6.38%) | 0/24 |
| `first_host=curationist.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=d-museum.kokugakuin.ac.jp` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=dao.crs.cuhk.edu.hk` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=diskoproject.kelsey.lsa.umich.edu` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=englishkyoto-seas.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=footwearresearchnetwork.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=gsrjournal.com` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=gutenberg.org` | 3/48 (6.25%) | 6/141 (4.26%) | 0/24 |
| `first_host=hierotopy.ru` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=islamicart.museumwnf.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=jnjr.div.ed.ac.uk` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=journal.sciencemuseum.ac.uk` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=journal.thewalters.org` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=journals.iaepan.pl` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=jwa.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=metmuseum.org` | 0/48 (0.00%) | 6/141 (4.26%) | 0/24 |
| `first_host=mlit.go.jp` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=museum.sinica.edu.tw` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=museum.wales` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=myjewishlearning.com` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=openaccess.iku.edu.tr` | 3/48 (6.25%) | 3/141 (2.13%) | 0/24 |
| `first_host=pmc.ncbi.nlm.nih.gov` | 0/48 (0.00%) | 6/141 (4.26%) | 0/24 |
| `first_host=posenlibrary.com` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=prm.web.ox.ac.uk` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=provanhall.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=religionswissenschaft.uzh.ch` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=resources.metmuseum.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=rubinmuseum.org` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=smithsonianmag.com` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=ucl.ac.uk` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=vrme.yale.edu` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_host=web.prm.ox.ac.uk` | 0/48 (0.00%) | 3/141 (2.13%) | 0/24 |
| `first_two` | 11/48 (22.92%) | 37/141 (26.24%) | 2/24 |
| `hybrid_0.1` | 42/48 (87.50%) | 0/141 (0.00%) | 18/24 |
| `hybrid_0.2` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_0.25` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_0.3` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_0.35` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_0.4` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_tail_0.1` | 45/48 (93.75%) | 0/141 (0.00%) | 21/24 |
| `hybrid_tail_0.2` | 48/48 (100.00%) | 0/141 (0.00%) | 24/24 |
| `hybrid_tail_0.25` | 48/48 (100.00%) | 0/141 (0.00%) | 24/24 |
| `hybrid_tail_0.3` | 48/48 (100.00%) | 0/141 (0.00%) | 24/24 |
| `hybrid_tail_0.35` | 48/48 (100.00%) | 0/141 (0.00%) | 24/24 |
| `hybrid_tail_0.4` | 48/48 (100.00%) | 0/141 (0.00%) | 24/24 |
| `label_odd` | 29/48 (60.42%) | 67/141 (47.52%) | 0/24 |
| `last_two` | 12/48 (25.00%) | 36/141 (25.53%) | 1/24 |
| `longest_two` | 21/48 (43.75%) | 27/141 (19.15%) | 0/24 |
| `odd_quote_grammar` | 18/48 (37.50%) | 0/141 (0.00%) | 0/24 |
| `place_or_date` | 15/48 (31.25%) | 3/141 (2.13%) | 0/24 |
| `post_tier_semicolon` | 12/48 (25.00%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.1` | 12/48 (25.00%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.2` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.25` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.3` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.35` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.4` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.5` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_both_lt_0.6` | 15/48 (31.25%) | 6/141 (4.26%) | 0/24 |
| `quote_both_lt_0.7` | 18/48 (37.50%) | 15/141 (10.64%) | 0/24 |
| `quote_entry_lt_0.1` | 12/48 (25.00%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.2` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.25` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.3` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.35` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.4` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.5` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_entry_lt_0.6` | 15/48 (31.25%) | 6/141 (4.26%) | 0/24 |
| `quote_entry_lt_0.7` | 18/48 (37.50%) | 15/141 (10.64%) | 0/24 |
| `quote_teaches_lt_0.1` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |
| `quote_teaches_lt_0.2` | 15/48 (31.25%) | 3/141 (2.13%) | 0/24 |
| `quote_teaches_lt_0.25` | 15/48 (31.25%) | 6/141 (4.26%) | 0/24 |
| `quote_teaches_lt_0.3` | 15/48 (31.25%) | 12/141 (8.51%) | 0/24 |
| `quote_teaches_lt_0.35` | 15/48 (31.25%) | 24/141 (17.02%) | 0/24 |
| `quote_teaches_lt_0.4` | 18/48 (37.50%) | 33/141 (23.40%) | 0/24 |
| `quote_teaches_lt_0.5` | 27/48 (56.25%) | 51/141 (36.17%) | 0/24 |
| `quote_teaches_lt_0.6` | 30/48 (62.50%) | 84/141 (59.57%) | 0/24 |
| `quote_teaches_lt_0.7` | 42/48 (87.50%) | 111/141 (78.72%) | 0/24 |
| `shortest_two` | 9/48 (18.75%) | 39/141 (27.66%) | 0/24 |
| `ungraded_citation_tail` | 15/48 (31.25%) | 0/141 (0.00%) | 0/24 |

## Assigned one-point mutation and detector

Mutation point: `fixture.py:18`, **only** `MODE = 'oracle'` -> `MODE = 'packet'` -> `MODE = 'oracle'`.

The pristine calibration uses the key to create correct fixture labels. It is a synthetic detector-positive calibration, **not** a claim that an oracle performed the source review. The mutation replaces that verdict origin with the packet-only program. Because the program classifies this dry-run set exactly, generated reports and transcripts are byte-identical between the correct-label calibration and the shortcut. The counter cannot tell those origins apart after SESSIONS is redirected.

Expected detector: SUPPORT should not substantiate source-reading work merely because correct-looking verdicts accompany page-naming calls. The observed SESSIONS-only probe accepts this work-skipping fixture. Frozen PROVENANCE blocks the fabricated sessions as designed; that baseline failure is not counted as a killed mutant.

Each phase was generated under a 60-second cap. The same `detect.py` invocation, under a 500-second outer cap, ran the frozen counter and the probe sequentially, each as `timeout 240 python3 -B <counter>` with cwd equal to the clone. The frozen invocation is the committed counter's canonical command with an absolute script path; neither its bytes nor any non-SESSIONS predicate was modified. Environment set `PYTHONDONTWRITEBYTECODE=1`, sandbox-local `TMPDIR`/`UV_CACHE_DIR`, and disabled automatic Python downloads. All six full stdout streams and exits are reproduced below. All six stderr streams were empty.

186 page-naming synthetic curl calls are present per fixture. Each command has a literal packet URL and this shape:

```text
timeout 20 curl --max-time 15 --max-filesize 2097152 --location --silent --output /dev/null '<literal first URL of packet block>'
```

Their synthetic tool-call cwd is the declared packet sandbox, satisfying the counter's CONFINED parser. They are not actual shell execution records. The real generation/detector shell commands all ran under this seat's own scratch directory. No page response was read or supplied to the classifier.

### Only permitted probe difference

```diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlKeyedLabelA3/fake-sessions/{seat}.jsonl"  # synthetic control fixture
 
 
 def tool_calls(transcript):
```

### Control receipt lines

```text
RECEIPT CtlKeyedLabelA3/pristine counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT(PROVENANCE=session-files=0);probe:none probe-sha256=c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5 probe-exit=0
RECEIPT CtlKeyedLabelA3/mutated counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT(PROVENANCE=session-files=0);probe:none probe-sha256=c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5 probe-exit=0
RECEIPT CtlKeyedLabelA3/restored counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT(PROVENANCE=session-files=0);probe:none probe-sha256=c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5 probe-exit=0
```

### Full counter outputs

#### pristine / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

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

#### pristine / probe

Counter sha256: `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5`.

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

#### mutated / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

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

#### mutated / probe

Counter sha256: `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5`.

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

#### restored / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

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

#### restored / probe

Counter sha256: `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5`.

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

## Restoration evidence

The mutation was restored before the restored detector run. Hashes are actual SHA-256 values, not tool snapshot tags:

| Object | Pristine | Mutated | Restored |
|---|---|---|---|
| Fixture driver | `76991aefc83acdf23016e563ce9ee994eedfda5c496870fe060656445fb84aaf` | `886385a2eca251ecdf2480a7f200f5a30ad9d707ad3d3a672b00cfbc9470ed9a` | `76991aefc83acdf23016e563ce9ee994eedfda5c496870fe060656445fb84aaf` |
| Canonical detector-input manifest | `2c22b932c458a25070ba4cc13bcf99a78bf6b6fcd71ce03d4428aacd3f2cbc9a` | `2c22b932c458a25070ba4cc13bcf99a78bf6b6fcd71ce03d4428aacd3f2cbc9a` | `2c22b932c458a25070ba4cc13bcf99a78bf6b6fcd71ce03d4428aacd3f2cbc9a` |
| Frozen counter | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` |
| Probe counter | `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5` | `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5` | `c92340dc2ccbfc1f0a70b73fd7e8c12b7f02f55151d08abf7ce6de78c26c09d5` |

The manifest is SHA-256 of the sorted compact JSON mapping every detector-input relative path to its file SHA-256. It covers reports, packets, key, planted rows, registry, committed-shape transcripts, their fake session copies, entry, SOURCES, captures, key-hash declaration and both counter files. All three recorded mappings were compared and are exactly equal; the restored driver's SHA-256 equals its pristine SHA-256. The fixture-source switch is therefore byte-exactly restored; the reports were already byte-identical across the mutation. This does not assert the disposable patched clone equals the unpatched lane revision.

## Bounds, tooling and artifact handoff

- Scratch measured **169 MiB**, below the 200 MB allocation cap as reported by `du -sm` (the allocation figure is 169 MiB, approximately 177 MB decimal). No full fixture clone was duplicated.
- All spawned processes were bounded and returned. No background job, service, subagent, other model runtime, or live reviewer was started. No process tree remains outstanding from this experiment.
- No host tool was installed or updated. Existing `uv 0.13.0` materialised **pypdf 5.4.0** from its official PyPI dependency into the sandbox-local uv cache for the frozen PDF locator; this is the counter's exact declared dependency, not a replacement parser. No pacman transaction or service action occurred.
- Reproducer files retained in the sandbox: `prepare.py`, `guess.py`, `evaluate.py`, `fixture.py` (restored), `detect.py`, `accept-d-probe.py`, `probe.diff`, `metrics.json`, `predictions.json`, `feature-table.md`, preparation hashes, and all six stdout/stderr/receipt JSON artifacts. Use the existing generated packets for reproduction; re-running preparation generates a new random layout.
- Only the assigned control/mutation probe was performed. No permanent source edit, contract change, integration, or additional verification is proposed or performed here.

Recorded UTC: 2026-10-23T07:12:22.303177+00:00.
