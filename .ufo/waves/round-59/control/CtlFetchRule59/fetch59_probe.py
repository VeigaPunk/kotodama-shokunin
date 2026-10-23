#!/usr/bin/env python3
"""Same bounded behavioral detector for pristine, mutant, restored frozen bytes.
Only *.fixture.test URLs are mapped at urllib's transport boundary to http.server.
The frozen locator, cache, root fallback, topic and SUPPORT tests otherwise execute.
"""
import argparse
from collections import Counter
import concurrent.futures
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
import urllib.request
import fixture_transport

HERE = Path(__file__).resolve().parent
ROOT = HERE / 'clone'
ENTRY = 'corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'
SUPPORT = '.ufo/waves/round-59/support'
STAMP = '20240102030405'
GAP_QUOTE = 'The stone was catalogued in a quiet museum before readers discussed protective history.'
TEACHES = 'Household amulet and charm traditions describe ceremonial protection for local wearers.'


def quote(index=0):
    return f'The amulet was carried by the household as a protective charm during ceremony number {index}.'


def capture(url, stamp=STAMP):
    return f'https://web.archive.org/web/{stamp}id_/{url}'


def cells(urls, sid='S600', q=None, teaches=TEACHES):
    return ['', sid, 'Synthetic fixture — ' + ' '.join(urls), 'docs', 'A', 'fixture',
            'body: "' + (q or quote()) + '"', teaches, 'mined', '2026-10-23', '365d', ENTRY, '']


def load_rowcheck(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'reports/round-59/rowcheck.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SyntheticCorpus:
    def __init__(self):
        self.saved = {}

    def put(self, relative, content):
        path = ROOT / relative
        if path not in self.saved:
            self.saved[path] = path.read_bytes() if path.exists() else None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode('utf-8') if isinstance(content, str) else content)

    def install(self):
        entry = '# Synthetic protective-object fixture (not a real knowledge entry)\n- topic: synthetic protective-object detector fixture\n- kind: fixture\n\n'
        extra = []
        for i in range(20):
            sid = f'S{600 + i}'
            extra.append('|'.join(cells([f'http://good{i:02d}.fixture.test/leaf'], sid=sid, q=quote(i))))
            entry += f'Household amulet and charm traditions describe ceremonial protection for local wearers ({sid}).\n'
        self.put(ENTRY, entry)
        self.put('corpus/SOURCES.md', (ROOT / 'corpus/SOURCES.md').read_text() + '\n' + '\n'.join(extra) + '\n')
        readme = (ROOT / 'corpus/README.md').read_text()
        readme = re.sub(r'^## myth-symbol/ \((\d+)\)$', lambda m: f'## myth-symbol/ ({int(m[1]) + 1})\n- `amulets-talismans-apotropaic-marks.md` — synthetic protective-object detector fixture', readme, flags=re.M)
        readme = re.sub(r'^Total knowledge entries: (\d+)\.$', lambda m: f'Total knowledge entries: {int(m[1]) + 1}.', readme, flags=re.M)
        def footer(match):
            counts = [int(value) for value in match[2].split('/')]
            counts[1] += 1
            return f'(total {int(match[1]) + 1} files; directory totals {"/".join(map(str, counts))}).'
        readme = re.sub(r'\(total (\d+) files; directory totals ([\d/]+)\)\.', footer, readme)
        self.put('corpus/README.md', readme)
        registry = {'members': [{'name': name, 'role': 'reviewer', 'agentId': 'synthetic-not-an-agent-' + name}
                                for name in ('FixtureA59', 'FixtureB59')]}
        key = {'seats': {name: {**{f'P{i + 1:02d}': f'S{600 + i}' for i in range(20)}, 'P21': 'PLANTED'}
                         for name in ('FixtureA59', 'FixtureB59')}}
        key_bytes = (json.dumps(key, sort_keys=True, indent=2) + '\n').encode()
        rows_bytes = b'# Synthetic planted control\nPLANTED: intentionally unsupported shortcut row.\n'
        self.put(SUPPORT + '/registry.json', json.dumps(registry, indent=2) + '\n')
        self.put(SUPPORT + '/planted-key.json', key_bytes)
        self.put(SUPPORT + '/planted-rows.md', rows_bytes)
        self.put('reports/round-59/planted-key.sha256', hashlib.sha256(key_bytes).hexdigest() + '\n')
        self.put('reports/round-59/planted-rows.sha256', hashlib.sha256(rows_bytes).hexdigest() + '\n')
        self.mode('positive')

    def mode(self, mode):
        for name in ('FixtureA59', 'FixtureB59'):
            packet = '# Explicitly synthetic blind-packet fixture\n'
            report = '# Explicitly synthetic verdict fixture; no reader was dispatched\n'
            for i in range(20):
                label = f'P{i + 1:02d}'
                shown = ('This completely different sentence has never been the landed source quote.'
                         if mode == 'wrong-quote' else quote(i))
                packet += f'\n### {label}\nquote: "{shown}"\n'
                verdict = 'NOT-SUPPORTED' if mode == 'all-false' else 'SUPPORTED'
                report += f'VERDICT {label} {verdict}\n'
            packet += '\n### P21\nquote: "An intentionally unsupported synthetic planted quote with enough normalised words."\n'
            plant_verdict = 'SUPPORTED' if mode == 'rubber-stamp' else 'NOT-SUPPORTED'
            report += f'VERDICT P21 {plant_verdict}\n'
            self.put(SUPPORT + '/packet-' + name + '.md', packet)
            self.put(SUPPORT + '/' + name + '.md', report)

    def restore(self):
        mismatches = []
        for path, original in reversed(list(self.saved.items())):
            if original is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(original)
            if (path.read_bytes() if path.exists() else None) != original:
                mismatches.append(str(path))
        return mismatches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--phase', required=True)
    args = parser.parse_args()
    outdir = HERE / ('run-' + args.phase)
    outdir.mkdir(exist_ok=True)
    ready, logfile = outdir / 'ready.json', outdir / 'http-get.jsonl'
    ready.unlink(missing_ok=True)
    server = subprocess.Popen(['timeout', '850', sys.executable, '-B', str(HERE / 'fixture_server.py'),
                               '--ready', str(ready), '--log', str(logfile)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
    fixture = SyntheticCorpus()
    cases = []
    failures = []
    observations = []
    server_evidence = {}
    restoration = []
    try:
        for unused in range(250):
            if ready.exists() and ready.stat().st_size:
                break
            if server.poll() is not None:
                raise RuntimeError('fixture server exited: ' + server.stderr.read().decode())
            time.sleep(0.02)
        origin = 'http://127.0.0.1:' + str(json.loads(ready.read_text())['port'])

        def events(tag):
            response = fixture_transport._RAW_OPEN(origin + '/events', timeout=10)
            with response:
                return [event for event in json.load(response) if event['run'] == tag]

        def probe(name, urls, expected, *, q=None, teaches=TEACHES, repeat=1, expected_counts=None, contract_only=False, race=False):
            fixture_transport.install(origin, name)
            module = load_rowcheck('probe_' + name.replace('-', '_'))
            row = cells(urls, q=q, teaches=teaches)
            entry = teaches + ' (S600).'
            if race:
                import threading
                barrier = threading.Barrier(2)
                def read_once(unused):
                    barrier.wait(timeout=5)
                    return module.check_row(row, entry)
                with concurrent.futures.ThreadPoolExecutor(2) as pool:
                    results = list(pool.map(read_once, range(2)))
            else:
                results = [module.check_row(row, entry) for unused in range(repeat)]
            requests = events(name)
            count = dict(Counter(event['url'] for event in requests))
            actual = {leg: ok for leg, (ok, detail) in results[0].items()}
            ok = all({leg: value[0] for leg, value in result.items()} == expected for result in results)
            if expected_counts is not None:
                ok &= count == expected_counts
            item = {'name': name, 'expected': expected, 'actual': actual, 'ok': ok,
                    'details': results[0], 'GET_counts': count, 'GETs': requests,
                    'expected_counts': expected_counts, 'repeat': repeat, 'contract_only': contract_only}
            (observations if contract_only else cases).append(item)
            if not ok and not contract_only:
                failures.append(name)
            print(f'PROBE {name} detector={"PASS" if ok else "FAIL"} legs=' + json.dumps(actual, sort_keys=True)
                  + ' GET_counts=' + json.dumps(count, sort_keys=True), flush=True)
            return item

        yes = dict.fromkeys(('LOCATE', 'BOILER', 'RELEVANCE', 'TOPIC'), True)
        no_location = {**yes, 'LOCATE': False, 'BOILER': False, 'TOPIC': False}
        for status in (403, 404):
            live = f'http://deny{status}.fixture.test/leaf'
            archived = capture(live)
            archive_root = f'https://web.archive.org/web/{STAMP}/http://deny{status}.fixture.test/'
            probe(f'live-{status}-listed-capture', [live, archived], yes,
                  expected_counts={live: 1, archived: 1, archive_root: 1})
        live = 'http://deny403.fixture.test/leaf'
        probe('live-403-no-capture', [live], no_location, repeat=2, expected_counts={live: 1})
        live = 'http://root403.fixture.test/leaf'
        root = 'http://root403.fixture.test/'
        fallback = 'https://web.archive.org/web/2026id_/http://root403.fixture.test/'
        probe('root-403-page-200-default-capture', [live], yes,
              expected_counts={live: 1, root: 1, fallback: 1})
        fallback = f'https://web.archive.org/web/{STAMP}id_/http://root403.fixture.test/'
        probe('root-403-page-200-listed-timestamp', [live, capture(live)], yes,
              expected_counts={live: 1, root: 1, fallback: 1})
        live = 'http://rootsfail.fixture.test/leaf'
        root = 'http://rootsfail.fixture.test/'
        fallback = 'https://web.archive.org/web/2026id_/http://rootsfail.fixture.test/'
        probe('both-roots-fail', [live], {**yes, 'BOILER': False},
              expected_counts={live: 1, root: 1, fallback: 1})
        live = 'http://reuse.fixture.test/leaf'
        probe('one-fetch-reused-across-legs-and-rows', [live], yes, repeat=2,
              expected_counts={live: 1, 'http://reuse.fixture.test/': 1})
        live = 'http://transient429.fixture.test/leaf'
        probe('transient-429-then-200', [live], yes, repeat=2,
              expected_counts={live: 2, 'http://transient429.fixture.test/': 1})
        live = 'http://always429.fixture.test/leaf'
        probe('persistent-429-error-reused', [live], no_location, repeat=2, expected_counts={live: 3})
        live = 'http://topicgap.fixture.test/leaf'
        probe('topic-window-negative', [live], {**yes, 'TOPIC': False}, q=GAP_QUOTE,
              teaches='Museum stone catalogues explain a protective history for curious readers.')
        live = 'http://race.fixture.test/leaf'
        probe('concurrent-one-fetch-contract', [live], yes, race=True, contract_only=True,
              expected_counts={live: 1, 'http://race.fixture.test/': 1})
        live = 'http://transient501.fixture.test/leaf'
        probe('transient-501-docstring-contract', [live], yes, repeat=2, contract_only=True,
              expected_counts={live: 2, 'http://transient501.fixture.test/': 1})

        fixture.install()
        for mode in ('positive', 'rubber-stamp', 'wrong-quote', 'all-false'):
            fixture.mode(mode)
            tag = 'support-' + mode
            env = os.environ.copy()
            env.update({'FETCH59_ORIGIN': origin, 'FETCH59_TAG': tag})
            command = ['timeout', '900', sys.executable, '-B', str(HERE / 'counter_driver.py')]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=env, timeout=895)
            (outdir / (tag + '.stdout')).write_text(result.stdout)
            (outdir / (tag + '.stderr')).write_text(result.stderr)
            failed_legs = re.findall(r'^(\w+) FAIL\b', result.stdout, re.M)
            last = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else '<no stdout>'
            expected_legs = [] if mode == 'positive' else ['SUPPORT']
            expected_exit = 0 if mode == 'positive' else 1
            ok = failed_legs == expected_legs and result.returncode == expected_exit and last == ('ACCEPT-C-59: PASS' if expected_exit == 0 else 'ACCEPT-C-59: FAIL')
            item = {'name': tag, 'expected_failed_legs': expected_legs, 'failed_legs': failed_legs,
                    'ok': ok, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
                    'command': command, 'GET_counts': dict(Counter(event['url'] for event in events(tag)))}
            cases.append(item)
            if not ok:
                failures.append(tag)
            print(f'CONTROL {tag} | claim C | exit {result.returncode} | {last} | failing legs: [{", ".join(failed_legs)}]', flush=True)
            print(result.stdout, end='', flush=True)
            if result.stderr:
                print('STDERR ' + result.stderr, flush=True)
    finally:
        restoration = fixture.restore()
        os.killpg(server.pid, signal.SIGTERM) if server.poll() is None else None
        try:
            server.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(server.pid, signal.SIGKILL)
            server.wait(timeout=10)
        server_evidence = {'timeout_pid': server.pid, 'returncode': server.returncode, 'alive': server.poll() is None}
        if restoration:
            failures.append('fixture-byte-restoration')
        print('SERVER_STOP ' + json.dumps(server_evidence, sort_keys=True), flush=True)
        print('FIXTURE_RESTORE exact=' + str(not restoration) + ' mismatches=' + json.dumps(restoration), flush=True)
    final = {'phase': args.phase, 'cases': cases, 'contract_observations': observations,
             'failures': failures, 'server': server_evidence, 'fixture_restoration_mismatches': restoration,
             'instrument_hashes': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                                   for p in ('reports/round-59/rowcheck.py', 'reports/round-59/accept-c.py')},
             'server_log': str(logfile)}
    (outdir / 'results.json').write_text(json.dumps(final, indent=2) + '\n')
    print('FETCH59-DETECTOR: ' + ('FAIL ' + ','.join(failures) if failures else 'PASS'), flush=True)
    return 1 if failures else 0

if __name__ == '__main__':
    sys.exit(main())
