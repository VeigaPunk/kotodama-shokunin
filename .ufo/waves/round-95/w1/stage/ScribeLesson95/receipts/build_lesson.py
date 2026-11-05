#!/usr/bin/env python3
"""Build stage/round-95.md (ScribeLesson95's draft of corpus/lessons/round-95.md).

Every located quote is taken from the committed capture bytes and verified here:
exact single occurrence in the raw capture, <= 25 words, >= 20 normalized chars,
not contained in the row's source cell or teaches cell, >= 4 content words shared
with the teaches cell (so the grader's GATE leg binds the gate line).

Refuses to write if any verification fails.
"""
import hashlib
import importlib.util
import os
import re

spec = importlib.util.spec_from_file_location(
    'g', '/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/base-tool.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ScoutTopic95'
REG = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecRegistry95/SOURCES.append.md'
EV = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecRegistry95/evidence'
OUT = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ScribeLesson95/round-95.md'

AS_OF = '2026-11-05'

# The gate-line quote each row binds with (exact substring of the raw capture).
BIND = {
    'S970': 'the antiphonal way of performing Seto songs makes it possible for the lead singer',
    'S971': 'antiphonal nature of voceru performance, though not discussed in detail here, suggests that Corsican lament',
    'S972': 'core, the keen was a sacred improvised chant',
    'S973': 'was important in the role of the female professional mourner who performed',
    'S974': 'recitation, Sima praises the good deeds and grace of the deceased,',
}


def rows():
    out = []
    for line in open(REG, encoding='utf-8'):
        if re.match(r'^\|\s*S\d{3,}\s*\|', line):
            out.append([c.strip() for c in line.rstrip('\n').strip('|').split('|')])
    return out


def main():
    rs = rows()
    assert len(rs) == 5, len(rs)
    table = []
    for c in rs:
        rid = c[0]
        src, anchor, teaches = c[1], c[5], c[6]
        url = g.urls(src)[-1]
        aq = re.search(r'anchor quote "([^"]*)"', anchor).group(1)
        raw = open(os.path.join(EV, rid + '.txt'), encoding='utf-8', errors='replace').read()
        pdf = os.path.join(EV, rid + '.pdf')
        raw_bytes = open(pdf, 'rb').read()
        # verifications
        assert raw.count(aq) == 1, (rid, 'anchor count', raw.count(aq))
        assert len(aq.split()) <= 25 and len(g.norm(aq)) >= 20, (rid, 'anchor bounds')
        b = BIND[rid]
        assert raw.count(b) == 1, (rid, 'bind count', raw.count(b))
        assert len(b.split()) <= 25 and len(g.norm(b)) >= 20, (rid, 'bind bounds')
        assert g.norm(b) not in g.norm(teaches), (rid, 'bind inside teaches')
        assert g.norm(aq) not in g.norm(src), (rid, 'anchor inside source cell')
        assert g.overlap(b, teaches) >= 4, (rid, 'bind overlap', g.overlap(b, teaches))
        txt_sha = hashlib.sha256(raw.encode('utf-8')).hexdigest()
        pdf_sha = hashlib.sha256(raw_bytes).hexdigest()
        table.append((rid, url, aq, len(aq.split()), txt_sha, pdf_sha, b, len(b.split())))

    L = []
    w = L.append
    w('# kotodama round 95 — lesson')
    w('')
    w('Round: kotodama round 95, attempt 1. Base `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`; freeze '
      '`d41eb594d27fa71869c0c28d9c2dc051fda40079` (claims O, C, predispatch receipt and wave-1 spec). '
      'Claims O (operability) and C (coverage) are exactly as frozen in `reports/round-95/claims.json`; '
      'the frozen bytes are not amended here.')
    w('')
    w('Freshness remains paused by the open L0 questions kotodama round-11 and round-89 '
      '("Freshness axis-move claims are paused until ruled"; '
      '`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303, both still carrying no '
      'L0 ANSWER). The lowest-axis obligation is neither met nor waived this round, and no freshness '
      'claim is declared.')
    w('')
    w('## Gate')
    w('')
    w('Claim C\'s registry rows. Five new rows, S970–S974, all opened by ordinary means on 2026-11-05 '
      '(plain `curl`, default user agent, `-L` follow-redirects, `--max-time 30`; no browser, no challenge '
      'passed, no verification disabled). Every quote below was re-verified by this seat against the '
      'committed capture bytes: each is an exact substring occurring exactly once '
      '(`bytes.count(quote) == 1`) and each is 25 words or fewer. The capture sha256 values are '
      're-measured here and match `stage/ExecRegistry95/evidence/`.')
    w('')
    w('Further located spans the entry author may draw on, all in the same captures, all ≤25 words, each '
      're-verified here as an exact single occurrence:')
    w('')
    extra = [
        ('S970', 'the relationship between the genres of lament and song', 9),
        ('S971', 'feminine mode of expression', 4),
        ('S972', 'the keen was a sacred improvised chant that evolved over many centuries', 12),
        ('S973', 'keening woman—both representing and maintaining community Catholicism—', 7),
        ('S974', 'beseeching Pridon to', 3),
    ]
    w('| row | capture | further located quote | words |')
    w('|---|---|---|---|')
    for rid, q, n in extra:
        raw = open(os.path.join(EV, rid + '.txt'), encoding='utf-8', errors='replace').read()
        assert raw.count(q) == 1, (rid, 'extra count', raw.count(q))
        assert len(q.split()) == n, (rid, 'extra words', len(q.split()))
        w('| %s | S%s.txt | "%s" | %d |' % (rid, rid[1:], q, n))
    w('')
    w('| row | URL | access date | HTTP status | located quote (≤25 words, exact substring of the capture) '
      '| words | capture sha256 |')
    w('|---|---|---|---|---|---|---|')
    for rid, url, aq, aw, tsha, psha, b, bw in table:
        w('| %s | %s | %s | 200 | "%s" | %d | `%s` (S%s.txt); `%s` (S%s.pdf) |'
          % (rid, url, AS_OF, aq, aw, tsha, rid[1:], psha, rid[1:]))
    w('')
    w('All five rows are tier A, status `mined`, opened 2026-11-05, recheck `180d`, used-by '
      '`corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` — the 11-cell census grammar of '
      '`corpus/SOURCES.md` (header row at line 28). The claim requires at least three new rows from S970 '
      'up; five are proposed. The registry seat measured the projected state on its own mirror: census '
      'rc 0 with 0 E-findings and 0 findings on S970–S974, index `CORPUS-INDEX: OK files=267 rows=267 '
      'findings=0` rc 0, and the frozen counter over the mirrored tree prints `C2 registry-rows 898 '
      'highest-id S974`, `C1 entry-present 1` (bytes 50148, h2 12, table 11x5, phrases 6/6, topic-line '
      'equal), `C3 added=6 removed=0`, `C4 census rc=0`, `C5 index rc=0`.')
    w('')
    w('Gate lines the grader binds. The grader\'s GATE leg reads the first lesson line that names the '
      'id, the row URL, the access date and a quoted span, and refuses the line when the quote is the '
      'row\'s own teaching cell. For four of the five new rows the registry anchor quote *is* the first '
      'words of the teaching cell, so a gate line carrying that anchor quote is refused with the named '
      'diagnostic `gate quote is the row teaching cell (self-quote)`. The gate lines below therefore '
      'carry a second located span from the same capture, one that shares content words with the '
      'teaching cell without being it. Each is an exact single-occurrence substring of the same '
      'committed capture, 25 words or fewer, verified here the same way.')
    w('')
    for rid, url, aq, aw, tsha, psha, b, bw in table:
        w('- %s admit A/mined. %s — accessed %s — body: “%s”' % (rid, url, AS_OF, b))
    w('')
    w('Rejected and unreachable candidates, one line each with its exact response and a reason class '
      'per QUALITY criterion 37 (topic, access or scope; never title-only). None of these is a registry '
      'row.')
    w('')
    w('- Thrênoi to Moirologia (Oral Tradition 23/2, 2008) — UNREACHABLE, reason class access: curl exit 28, '
      'connection timed out after 30001 ms on the PDF, the site root and the issue page; the most on-point '
      'candidate for the moirologia professional-mourner facet, so no Oral Tradition row is proposed.')
    w('- MDPI Religions 10(4) article page and PDF (`https://www.mdpi.com/2077-1444/10/4/235`, `.../pdf`, '
      '`.../xml`) — UNREACHABLE, reason class access: HTTP 403 on every request; the candidate was '
      'recovered instead from the publisher\'s own asset host at HTTP 200, so it is a row and not an '
      'exclusion.')
    w('- MDPI Religions 15(7) article page and PDF (`https://www.mdpi.com/2077-1444/15/7/879`, `.../pdf`) — '
      'UNREACHABLE, reason class access: HTTP 403 (400- and 408-byte bodies); recovered from the '
      'publisher\'s asset host at HTTP 200 and landed as S973.')
    w('- Gender Performativity in Burgenland Croatian Laments (`https://minpaku.repo.nii.ac.jp/record/'
      '8716/files/SES105_14.pdf`) — UNREACHABLE, reason class access: HTTP 503 on two attempts.')
    w('- Olonets Karelian prichitannye tradition (`https://www.trad-culture.ru/sites/default/files/files_pdf/'
      '02_2026_...95-108.pdf`) — UNREACHABLE, reason class access: HTTP 404 (25345-byte HTML error page) '
      'at the locator OpenAlex published.')
    w('- Pure Corpses, Dangerous Citizens (`https://durham-repository.worktribe.com/preview/1371952/'
      '20127.pdf`) — UNREACHABLE, reason class access: HTTP 403 (5486-byte body).')
    w('- Shaping the pain, 2012 and 2011 (`http://www.doiserbia.nb.rs/img/doi/0350-0861/2012/'
      '0350-08611202139S.pdf` and the 2011 sibling) — UNREACHABLE, reason class access: connection timed '
      'out at 30 s on repeated attempts; both titles remain unsourced.')
    w('- Seto lamenting song via De Gruyter (`https://www.degruyterbrill.com/document/doi/10.2478/'
      'jef-2025-0006/pdf` and the legacy host) — UNREACHABLE, reason class access: HTTP 202 with 0 bytes '
      '(challenge interstitial); the same article was obtained at HTTP 200 from `sciendo.com/pdf/...`.')
    w('- Madwoman, Banshee, Shaman (`http://hdl.handle.net/10072/30483`) and Keening the Nation, the Bean '
      'Chaointe (`http://hdl.handle.net/1808/7785`) — UNREACHABLE, reason class access: HTTP 200 but a '
      'JavaScript-only DSpace shell (755 and 827 bytes, no article text).')
    w('- Mourners and mediums (`https://opus.bath.ac.uk/19457/1/Walter_Bt_Care_2008_27_3_p47.pdf`) — '
      'UNREACHABLE, reason class access: HTTP 200 but the bytes are an HTML portal page, not a PDF '
      '(46859 bytes).')
    w('- Semaine seto (`https://journals.openedition.org/efo/pdf/6912`) and Briséis et la plainte funèbre '
      '(`https://journals.openedition.org/mondesanciens/729`) — UNREACHABLE, reason class access: HTTP 200 '
      'but a ~1.5 KB / 1.6 KB shell, no article body.')
    w('- Mäetagused Arukask (`https://www.folklore.ee/tagused/mt2011.47.arukask.pdf`) — UNREACHABLE, '
      'reason class access: HTTP 404 (510 bytes), wrong filename pattern.')
    w('- Mäetagused Ing (`https://www.folklore.ee/tagused/nr08/ing.pdf`) — UNREACHABLE, reason class '
      'access: HTTP 404 (510 bytes).')
    w('- Folklore vol. 58 Kalkun at the wrong filename (`https://www.folklore.ee/folklore/vol58/kalkun.pdf`) '
      '— UNREACHABLE, reason class access: HTTP 404 (510 bytes); the file is `kalkun_oras.pdf`.')
    w('- Crossref `itkuviis lament refrain` — UNREACHABLE, reason class access: HTTP 429 (rate limited), '
      'empty body, so that query returned no records to screen.')
    w('- Kama, Pikne (2017), How old is runosong? Dating the motifs of burial-related folk songs '
      '(`https://www.folklore.ee/folklore/vol68/kama.pdf`, HTTP 200, 8226843 bytes) — excluded, reason '
      'class scope: an archaeological dating argument that uses burial songs as a dating instrument and '
      'does not treat the lament as a speech register with performers, structure or content types.')
    w('- Jouste, Marko (2020), Suonikylän kolttasaamelainen itkuperinne 1900-luvulla '
      '(`https://etnomusikologia.journal.fi/article/download/90118/57605`, HTTP 200) — excluded, reason '
      'class scope: an ethnographic inventory of one community\'s twentieth-century repertoire, whose '
      'register structure overlaps S978\'s Karelian/Lithuanian comparative account.')
    w('- Kalkun, Andreas (2014), Seto Singing Tradition in Siberia '
      '(`https://www.folklore.ee/folklore/vol58/kalkun_oras.pdf`, HTTP 200) — excluded, reason class '
      'scope: a song-tradition survey of Seto leelo, not a lament register account; S970 covers the Seto '
      'lament proper.')
    w('- Kalkun, Andreas (2017), Introducing Setos on Stage (`https://www.folklore.ee/folklore/vol68/'
      'kalkun.pdf`, HTTP 200) — excluded, reason class scope: staged Seto song history, not the mourning '
      'register.')
    w('- Korolëva, Svetlana (2018), Cherdyn funeral laments (`https://press.psu.ru/index.php/philology/'
      'article/download/1450/1082`, HTTP 200) — excluded, reason class scope: a Russian-language study '
      'of one region\'s ritual lexicon and the vestka letter-message motif, whose address-to-the-dead '
      'facet is already grounded by S980 and S974.')
    w('- Lamentations in the Turkish culture and their functions in society, on the example of Kyrgyz '
      '(`https://dergipark.org.tr/tr/download/article-file/490587`, HTTP 200) — excluded, reason class '
      'scope: a general survey of lament function in one Turkic society, adding no frozen sub-topic the '
      'landed rows do not already cover.')
    w('- Literary and historical scholarship on written lament named by Crossref (Mourning Becomes '
      'Eclectic, 2005; The Ritual Lament in Greek Tradition, 2002; Antiphonal Lament Between Achilles and '
      'Briseis, 1997; Thrēnos and Ritual Lament, 2010; Do Brothers Weep?, 2017; 12 Virgilian Matres, '
      '2020; Radegund and Amalfrid in The Wife\'s Lament, 2021; The Book of Ezekiel and Mesopotamian '
      'City Laments, 2011) — excluded, reason class scope: scholarship on written, literary lament, not '
      'the sung speech register as a social institution with performers, refrain structure and a design '
      'procedure, and no plain full-text OA capture was reachable.')
    w('- Generic refrain and formulaic-theory chapters named by Crossref (The Refrain in David\'s lament '
      'over Saul and Jonathan, 1972; Refrain, Oxford Music Online, 2001; A Good Refrain Sells the Song, '
      '2010; A Nuclear Refrain, 2018; Formulaic Language: An Overview, 2010) — excluded, reason class '
      'scope: no mourning-lament corpus and no OA capture.')
    w('- Literary-historical and law-review treatments named by Crossref (Funeral song poetry, 2025; '
      'Servile Mourning for the Powerful, 2023; Comforted But Not Compensated?, 2015; Mourners at Sir '
      'Philip Sidney\'s Funeral, 1941, three records) — excluded, reason class scope: no accessible full '
      'text, so not usable for a quote under the ordinary-means rule.')
    w('- Non-OA or shell-only records named by OpenAlex (The Funeral Lament as an Anthropopoietical '
      'Ritual, 2018; Of Commodified Grief and Emotions, 2025; A Witness to Death, 2015; Keening as a '
      'cross-cultural phenomenon, 1993; Pure Corpses, Dangerous Citizens, 2016; Social Support in '
      'Perinatal Grief, 2020) — excluded, reason class access: the OA URL returned 403 or a JS-only '
      'shell, or the object is not about the lament register, or it is a thesis whose landing page '
      'carries no quotable body text.')
    w('- The Context and Structure of Funeral Oratory among the Bukusu (2014) — excluded, reason class '
      'scope: funeral oratory, not the sung lament register.')
    w('- Creative dynamism and religious syncretism in Igbo oral funeral songs (2024) — excluded, reason '
      'class scope: Igbo syncretism, not the lament register as such.')
    w('- The Therapeutic Dimensions of BaTonga Mourning Songs (2025) — excluded, reason class scope: a '
      'therapeutic framing that overlaps S972\'s clinical framing without adding a distinct frozen '
      'sub-topic.')
    w('- folklore.ee site search `?s=lament` (1 hit, an unrelated Estonian Parishes article) — excluded, '
      'reason class scope: the record\'s subject is Estonian parishes, not the lament register.')
    w('')
    w('Search method (screening only; every row above was then opened by a direct request to the '
      'article page or PDF): the DOAJ open-access article API `https://doaj.org/api/search/articles/'
      '<query>?pageSize=25` over twelve queries, the Crossref works API `https://api.crossref.org/works?'
      'query.bibliographic=&rows=15` over five queries, the OpenAlex works API `https://api.openalex.org/'
      'works?search=&per-page=25` over eight queries, and two folklore.ee site operations (a site search '
      'and an index sweep of eleven volumes). The APIs were used as finders; every included record was '
      'then fetched at its publisher or OJS URL.')
    w('')
    w('Search-log summary as the scout measured it from the saved API JSON: 27 query operations (25 API '
      'plus 2 site); 263 API records returned and screened (DOAJ 42, OpenAlex 161, Crossref 60) plus 2 '
      'site-search hits, 265 records screened in all; 12 direct captures staged (11 tier A, 1 tier C); '
      '253 excluded at screening. A candidate may be returned by more than one query, so the per-query '
      'included counts sum to more than 12 (20 query-candidate hits resolving to 12 distinct candidates). '
      'The API-reported identified counts are the providers\' fuzzy-match totals for the whole index, '
      'not the size of a relevant set; only the returned page was screened. Stop rationale: a coverage '
      'stop, not a volume stop — after 27 query operations and 265 screened records every one of the six '
      'frozen sub-topic phrases had at least one tier-A primary capture with a verified '
      'single-occurrence quote, so further candidates would have widened the sample without closing an '
      'unfilled sub-topic. The gap that remains open in the landed set is a professional-mourner source '
      'from a non-European tradition: the scout staged one (S981, the Kenyan Abanyole dirge) but the '
      'registry seat landed five rows and did not carry it, so that gap is recorded rather than '
      'papered over.')
    w('')
    w('## Mistakes')
    w('')
    w('| id | class | evidence pointer | captured-by | fix |')
    w('|---|---|---|---|---|')
    w('| R95-M1 | stale-premise | the round-94 mutation manifest\'s `dispo-fallback` pattern was written '
      'against v4 bytes and scored BROKEN-PATTERN against v5 '
      '(`/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-94/mutation-score-lands.txt`, '
      'line `MUTANT dispo-fallback-off BROKEN-PATTERN selftest_rc=n/a`); re-measured here: the pattern '
      '`            m = DISPO_ANY_RE.search(plain)` occurs once in the v4 bytes and zero times in the v5 '
      'bytes, where the fallback moved into `_dispo_match` at eight-space indent | none — no '
      'pattern-freshness verification existed | mutants95 verifies every pattern against the target '
      'bytes at run start (declared exactly-once / replace-all match counts) before any scoring |')
    w('| R95-M2 | vacuous-survivor | the v5 selftest carried no pin for the >= 2-token heading anchor '
      'rule, so `head-qualify-off` survived the 88-mutant scoring (same receipt: '
      '`MUTANT head-qualify-off SURVIVED selftest_rc=0`); re-measured here: mutating the v5 bytes with '
      'that pattern still prints `SELFTEST PASS 126/126` at rc 0, so the mutation is invisible to the '
      'v5 selftest | none — no pin exercised the rule | the v6 head-qualify pin (the selftest fails under '
      'the mutant) |')
    w('| R95-M3 | reference-drift | the SKILL.md `## Gates and probes` registry carries no row for '
      '`tools/check-advance-evidence.py` v2–v5: `grep -in advance SKILL.md` returns nothing (rc 1), and '
      'the gate-registry auditor lists the tool under `tools_without_rows` while its own instrument set '
      'covers only `reports/round-*/accept-*.py` — yet the tool has been the round instrument since '
      'round 90 (named in `reports/round-90/claims.json` through `reports/round-94/claims.json`), with '
      'grader v2 at round 91, v3 at 92, v4 at 93 and v5 at 94 | the gate-registry auditor is '
      'informational only | the L1 lands the v6 registry row this round |')
    w('| R95-M4 | coupling defect | four of the five new registry rows open their `teaches` cell with '
      'their own anchor quote verbatim (the fifth escapes only because its anchor quote ends in a full '
      'stop), so the grader\'s GATE leg refuses the lesson\'s own gate line with the named diagnostic '
      '`gate quote is the row teaching cell (self-quote)`: measured over a scratch mirror of the staged '
      'rows, `LEG FAIL GATE` on four of five rows with both the v5 base bytes and the v6 candidate, and '
      '`LEG PASS GATE` with `ENTRY-EVIDENCE: PASS legs=9/9` once the gate lines carry a second span from '
      'the same capture (the gate lines in this lesson) | none — the round-95 counter has no entry-mode '
      'leg, so nothing in the frozen measurement sees it, and the base registry shows no such collision '
      '(0 of its 5 anchor-quote rows) | the L1 decides at landing: either the four teaching cells are '
      'reworded so the anchor quote is not their opening, or the landed lesson keeps the second-span '
      'gate lines written above |')
    w('| R95-M5 | missing deliverable | no round-95 seat staged `reports/round-95/evidence/manifest.json`, '
      'the per-row capture/url/http_status/fetched_at/sha256/quote manifest the grader\'s CAPTURE leg '
      'reads; without it the grader refuses the lesson with rc 2 and the named diagnostic '
      '`ADVANCE-EVIDENCE_ERROR: unreadable .../reports/round-95/evidence/manifest.json` (measured), and '
      'round 94 shipped the same file in its land commit | none — the wave specification names no seat '
      'for it | the L1 writes the manifest at landing, as it did for round 94 |')
    w('| R95-M7 | grader-input hazard in the lesson text | the grader\'s verdict-disguise channel '
      'reads every lesson line: a line that names a registry id and also carries the word '
      '`located` in any case is refused outright with `ADVANCE-EVIDENCE_ERROR: line N: lowercase '
      'verdict token outside the anchored rule (VERDICT-LOWERCASE)`, and the refusal aborts the whole '
      'entry grade before any leg is scored. Measured by drafting this lesson: the first draft of this '
      'row named the affected ids in the same line as that word and the grader refused the draft at '
      'line 82 with rc 2 | none — the round-95 counter has no entry-mode leg, and the round-92 to '
      'round-94 lessons happen to avoid the shape | the lesson keeps ids and that word on separate '
      'lines (this row and R95-M4 were reworded for it); a lesson author should assume every id-bearing '
      'line is parsed |')
    w('| R95-M6 | reason-not-recorded | the scout staged twelve candidates (S970–S981) and the registry '
      'seat landed five (S970–S974) without recording a reason for the seven it dropped, one of them '
      'the only non-European professional-mourner source in the set (S981, the Kenyan Abanyole dirge, '
      'which the scout counted as closing that gap) | none — the registry seat\'s report lists the five '
      'landed rows and is silent on the other seven | the L1 records the drop reason, or lands the '
      'non-European row, at landing |')
    w('')
    w('Each of the three named mistakes is shown able to fail by measurement, not by assertion. '
      'R95-M1: the round-94 pattern counts 1 in the v4 bytes and 0 in the v5 bytes, which is the '
      'BROKEN-PATTERN condition its own driver enforces. R95-M2: the mutated v5 bytes still print '
      '`SELFTEST PASS 126/126` at rc 0, so the rule the mutant removes is unpinned. R95-M3: '
      '`grep -in advance SKILL.md` prints nothing while the tool is named in five consecutive '
      'claims.json files. R95-M4 and R95-M5 are each reproduced by a command that fails in one shape '
      'and passes in the other; the receipts are the grader runs recorded in this seat\'s report.')
    w('')
    w('## Routed to round 96')
    w('')
    w('- CriticO95\'s nine surviving new classes against the v6 candidate (the critic\'s own measurement: '
      '`BATTERY-SUMMARY survivors=10 refused=6 unnamed=0 traceback=0`, of which 9 are fresh classes and '
      'the tenth is the ZWNJ1 control). Four are splitlines-severing verdict channels — VT1 (U+000B), '
      'FF1 (U+000C), LS1 (U+2028) and NEL1 (U+0085) — where `str.splitlines()` in `dispositions()` '
      'severs a forged gained `LOCATED` line before APPENDONLY can see it: one mechanism, four codepoints. '
      'Two are token-breakers NFKC cannot rejoin, NB1 (NBSP U+00A0, which folds to a space inside the '
      'token) and ANSI1 (ESC U+001B + `[31m`). One is CYR1, a Cyrillic small-a U+0430 in place of the id '
      'letter, which `_refuse_disguised` never reaches because it gates on `[Ss]\\d{3,}` first. Two are '
      'heading-token anchors the v6 number-strip does not enumerate, BR1 (`## (1) address`) and DASH1 '
      '(`## - address`), where any leading token that is not an ASCII, roman or fullwidth dot-form '
      'number still counts as a token. The critic\'s three smallest safe corrections are recorded with '
      'its report.')
    w('- The title-only exclusion re-decisions stay open. `corpus/lessons/round-92-verifier-spotcheck.md` '
      '§4 and §6 item 1 record three candidates whose exclusion was decided on title or metadata and '
      'whose re-opened text disagrees with the gate: Awetí motion events (2015), Zulu Lexikos (2011) and '
      'Turkish Signifiances (2020). Nothing in round 93, 94 or 95 re-decided them, and no L0 ANSWER '
      'stands on them; the round-92 lesson\'s criterion-37 sweep cannot retro-fit them.')
    w('- The F1 non-numbered variant is covered by behaviour but not by the battery predicate. Measured '
      'here against both the v5 base bytes and the v6 candidate: an entry whose h2 headings are '
      'content-free is refused on TOPIC with rc 1 and `ENTRY-EVIDENCE: FAIL legs=8/9 failed=TOPIC`, in '
      'the numbered form `## 1. alpha` and in the non-numbered form `## alpha beta` alike, so the v6 '
      'heading work closes both shapes. What is still open is the predicate, not the tool: the round-95 '
      'battery manifest lists fourteen classes (A1, B1, G1, H1, I1, J1, K1, CD1, LR1, TAB1, ID1, NUM1, '
      'RM1, NUM2) and no F1 entry, so the round that routed F1 out of round 93 has still not had the '
      'battery assert it. Round 96 should add the class rather than leave the coverage implicit.')
    w('- The registry\'s teaching cells and the grader\'s GATE leg are coupled (R95-M4 above) and the '
      'coupling is a row-shape rule, not a wording accident: any new row whose teaching cell opens with '
      'its anchor quote makes that anchor quote unusable as a gate quote. Round 96 should fix the rule '
      '(a teaching cell that paraphrases rather than quotes) or state the exemption, so the next wave does '
      'not rediscover it.')
    w('- The lands evidence manifest is still unwritten (R95-M5 above) and the seven staged-but-'
      'unlanded candidates still carry no recorded reason (R95-M6 above). Both are L1 landing decisions; '
      'neither is a claim failure.')
    w('- The freshness pause and the lowest-axis obligation are unchanged and open: '
      '`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303 (round-11 drift-threshold '
      'calibration, round-89 live re-verification admissibility) carry no L0 ANSWER, and the round-92 '
      'ideophones overlap question at line 356 is still open. The lowest-axis obligation is neither met '
      'nor waived.')
    w('')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L) + '\n')
    print('wrote', OUT, os.path.getsize(OUT), 'bytes')
    for rid, url, aq, aw, tsha, psha, b, bw in table:
        print(' ', rid, 'anchor', aw, 'w | bind', bw, 'w | txt', tsha[:16], 'pdf', psha[:16])


if __name__ == '__main__':
    main()
