#!/usr/bin/env python3
"""Round-89 supplementary audit of the REAL landing against the survivor
classes the wave found (ReviewerCounter H1-H4/M1-M4, CriticClaims 2-3).
Not a frozen leg and not admission evidence by itself: it reads committed
bytes at --lands with `git show` and reports each check's observation.

Usage: audit89.py --root LANE --base REV --lands REV --out JSON
"""
import argparse, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measure89 as m  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--root', required=True)
ap.add_argument('--base', required=True)
ap.add_argument('--lands', required=True)
ap.add_argument('--out', required=True)
a = ap.parse_args()


def show(rev, path):
    p = subprocess.run(['git', '-C', a.root, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return p.stdout.decode('utf-8', 'replace') if p.returncode == 0 else None


cfg = json.loads(show(a.lands, 'reports/round-89/claims.json'))
pop = cfg['F']['population']
src = show(a.lands, 'corpus/SOURCES.md')
ids = [l.strip().strip('|').split('|')[0].strip() for l in src.splitlines() if m.ROW_RE.match(l)]
rows = m.rows(src)
dup = sorted({i for i in ids if ids.count(i) > 1})
fman = json.loads(show(a.lands, cfg['F']['manifest']))['rows']
cman = json.loads(show(a.lands, cfg['C']['manifest']))['rows']
lesson = show(a.lands, cfg['lesson'])
entry = show(a.lands, cfg['C']['entry'])
iso = re.compile(r'^2026-11-04T\d\d:\d\d:\d\d[+-]\d\d:\d\d$')
checks = {}
checks['H1_duplicate_registry_ids'] = dup
checks['M1_capture_paths_outside_round_dirs'] = sorted(
    [k for k, v in fman.items() if not v['capture'].startswith('reports/round-89/rechecks/')] +
    [k for k, v in cman.items() if not v['capture'].startswith('reports/round-89/evidence/')])
checks['H3_wayback_urls'] = {k: v['url'] for k, v in list(fman.items()) + list(cman.items()) if 'web.archive.org' in v['url']}
checks['M4_fetched_at_not_full_local_iso'] = sorted(k for k, v in list(fman.items()) + list(cman.items()) if not iso.match(v['fetched_at']))
checks['H2_quote_is_substring_of_own_source_cell'] = sorted(k for k, v in fman.items() if m.contains(rows[k][1], v['quote']))
checks['H2_quote_word_counts'] = {k: len(v['quote'].split()) for k, v in fman.items()}
checks['M2_not_located_variants_in_lesson'] = re.findall(r'(?i)\bnot[ _]located\b|\bnot-located\b', lesson)
checks['M3_gitattributes_under_corpus'] = show(a.lands, 'corpus/.gitattributes') is not None
checks['C_entry_cites_population_ids'] = sorted(set(re.findall(r'\bS\d{3,}\b', entry)) & set(pop))
checks['H4_entry_topic_term_count'] = len(re.findall(r'(?i)evidential', entry))
ag = json.loads(show(a.lands, 'reports/round-89/rechecks/refetch-agreement.json'))
checks['F_independent_refetch_agreement'] = '%d/%d' % (ag['agree'], ag['total'])


def sh(t, n=8):
    w = re.sub(r'[^\w]+', ' ', t.lower()).split()
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


es = sh(entry)
checks['C3_8word_shingle_overlap'] = {p: len(es & sh(show(a.base, 'corpus/knowledge/linguistics/%s.md' % p) or ''))
                                     for p in ('semantics-pragmatics', 'syntax-typology', 'conlang-methodology',
                                               'semantic-fields-lexicon-building', 'morphological-typology')}
checks['C_base_sections_on_topic'] = [l for l in subprocess.run(
    ['git', '-C', a.root, 'grep', '-n', '-i', '-E', '^## .*evidential', a.base, '--', 'corpus/knowledge'],
    capture_output=True).stdout.decode().splitlines()]
clean = (not dup and not checks['M1_capture_paths_outside_round_dirs'] and not checks['M4_fetched_at_not_full_local_iso']
         and not checks['M3_gitattributes_under_corpus'] and not checks['C_entry_cites_population_ids']
         and ag['agree'] == ag['total'])
json.dump(dict(base=a.base, lands=a.lands, checks=checks, structural_classes_clear=clean,
               note='H2 rows listed are judged in the lesson (S032 title-level scope); H3 lists every archive-backed row'),
          open(a.out, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(dict(structural_classes_clear=clean, **{k: checks[k] for k in ('H1_duplicate_registry_ids', 'H3_wayback_urls', 'H2_quote_is_substring_of_own_source_cell', 'F_independent_refetch_agreement', 'C3_8word_shingle_overlap', 'C_base_sections_on_topic')}), ensure_ascii=False, indent=0))
