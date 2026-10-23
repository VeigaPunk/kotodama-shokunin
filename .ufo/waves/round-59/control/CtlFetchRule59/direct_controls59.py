#!/usr/bin/env python3
"""Score local no-reader controls with literal frozen-counter CLI, no urllib patch."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from fetch59_probe import SyntheticCorpus, HERE, ROOT

parser = argparse.ArgumentParser()
parser.add_argument('--phase', required=True)
args = parser.parse_args()
outdir = HERE / ('direct-' + args.phase)
outdir.mkdir(exist_ok=True)
ready, logfile, casefile = outdir / 'ready.json', outdir / 'http-get.jsonl', outdir / 'case.txt'
ready.unlink(missing_ok=True)
casefile.write_text('startup')
server = subprocess.Popen(['timeout', '850', sys.executable, '-B', str(HERE / 'direct_server59.py'),
                           '--ready', str(ready), '--log', str(logfile), '--case', str(casefile)],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
fixture = SyntheticCorpus()
results = []
restoration = []
try:
    for unused in range(250):
        if ready.exists() and ready.stat().st_size:
            break
        if server.poll() is not None:
            raise RuntimeError('server stopped: ' + server.stderr.read().decode())
        time.sleep(0.02)
    ports = json.loads(ready.read_text())['ports']
    fixture.install()
    sources = (ROOT / 'corpus/SOURCES.md').read_text()
    for i, port in enumerate(ports):
        sources = sources.replace(f'http://good{i:02d}.fixture.test/leaf', f'http://127.0.0.1:{port}/leaf')
    fixture.put('corpus/SOURCES.md', sources)
    for mode in ('positive', 'rubber-stamp', 'wrong-quote', 'all-false'):
        fixture.mode(mode)
        casefile.write_text(mode)
        env = {k: v for k, v in os.environ.items() if not k.startswith('FETCH59_')}
        command = ['timeout', '900', sys.executable, '-B', 'reports/round-59/accept-c.py']
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=895)
        (outdir / (mode + '.stdout')).write_text(result.stdout)
        (outdir / (mode + '.stderr')).write_text(result.stderr)
        failed = re.findall(r'^(\w+) FAIL\b', result.stdout, re.M)
        last = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else '<no stdout>'
        name = mode + ('-MEETS-COUNTER' if last == 'ACCEPT-C-59: PASS' else '-MEETS-MECHANICAL' if failed == ['SUPPORT'] else '')
        requests = [json.loads(line) for line in logfile.read_text().splitlines()]
        requests = [event for event in requests if event['case'] == mode]
        data = {'name': name, 'mode': mode, 'exit': result.returncode, 'last': last, 'failed_legs': failed,
                'stdout': result.stdout, 'stderr': result.stderr, 'command': command,
                'GET_counts': dict(Counter(event['url'] for event in requests))}
        results.append(data)
        print(f'CONTROL {name} | claim C | exit {result.returncode} | {last} | failing legs: [{", ".join(failed)}]', flush=True)
        print(result.stdout, end='', flush=True)
        if result.stderr:
            print(result.stderr, flush=True)
finally:
    restoration = fixture.restore()
    if server.poll() is None:
        os.killpg(server.pid, signal.SIGTERM)
    try:
        server.wait(timeout=10)
    except subprocess.TimeoutExpired:
        os.killpg(server.pid, signal.SIGKILL)
        server.wait(timeout=10)
    server_evidence = {'timeout_pid': server.pid, 'returncode': server.returncode, 'alive': server.poll() is None}
    print('SERVER_STOP ' + json.dumps(server_evidence, sort_keys=True), flush=True)
    print('FIXTURE_RESTORE exact=' + str(not restoration) + ' mismatches=' + json.dumps(restoration), flush=True)
summary = {'phase': args.phase, 'controls': results, 'server': server_evidence,
           'fixture_restoration_mismatches': restoration,
           'instrument_hashes': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                                 for p in ('reports/round-59/rowcheck.py', 'reports/round-59/accept-c.py')}}
(outdir / 'results.json').write_text(json.dumps(summary, indent=2) + '\n')
print('DIRECT59-CONTROLS: RECORDED', flush=True)
