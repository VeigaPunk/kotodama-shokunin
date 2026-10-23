#!/usr/bin/env python3
"""Ordinary public GET observations; no challenge solving, no transport substitution."""
import concurrent.futures
import importlib.util
import json
import pathlib
import re
import sys
import threading
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent / 'clone'
lock = threading.Lock()
events = []
local = threading.local()
raw_open = urllib.request.urlopen

def traced(request, *args, **kwargs):
    url = request.full_url if hasattr(request, 'full_url') else request
    try:
        response = raw_open(request, *args, **kwargs)
    except Exception as error:
        with lock:
            events.append({'case': getattr(local, 'case', '?'), 'url': url,
                           'status': getattr(error, 'code', None), 'error': type(error).__name__})
        raise
    with lock:
        events.append({'case': getattr(local, 'case', '?'), 'url': url,
                       'status': response.status, 'content_type': response.headers.get('Content-Type', '')})
    return response

urllib.request.urlopen = traced

cases = [
    ('real-met-listed',
     ['https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu',
      'https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu'],
     'Amulets with images of his full body or, more often, just his head, were common in the early first millennium B.C.'),
    ('real-met-unlisted',
     ['https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu'],
     'Amulets with images of his full body or, more often, just his head, were common in the early first millennium B.C.'),
    ('real-met-object-listed',
     ['https://www.metmuseum.org/art/collection/search/312342',
      'https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342'],
     'may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels'),
    ('real-nt-page-root',
     ['https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines'],
     'Aboriginal names for geographic or topographic features are preferred'),
    ('real-public-404', ['https://example.com/fetch59-missing-immutable-control'],
     'The amulet was carried by the household as a protective charm during ceremony number 0.'),
    ('real-teara-403-listed',
     ['https://teara.govt.nz/en/taniwha/print',
      'https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print'],
     'They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided.'),
    ('real-teara-403-unlisted',
     ['https://teara.govt.nz/en/taniwha/print'],
     'They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided.'),
]
if len(sys.argv) == 3 and sys.argv[1] == '--only':
    cases = [case for case in cases if sys.argv[2] in case[0]]

def probe(case):
    name, urls, quote = case
    local.case = name
    spec = importlib.util.spec_from_file_location('public_' + name.replace('-', '_'), ROOT / 'reports/round-59/rowcheck.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    located, detail = module.locator.locate(urls, quote)
    boiler = module.boiler(detail if located else '', quote, urls)
    repeated = module.locator.locate(urls, quote)
    return {'case': name, 'urls': urls, 'quote': quote, 'LOCATE': [located, detail],
            'BOILER': list(boiler), 'repeat_LOCATE': list(repeated),
            'cache_entries': len(module._CACHE)}

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(probe, cases))
for result in results:
    result['GETs'] = [event for event in events if event['case'] == result['case']]
    print(json.dumps(result, ensure_ascii=False), flush=True)
print('PUBLIC-FETCH-59: OBSERVED', flush=True)
