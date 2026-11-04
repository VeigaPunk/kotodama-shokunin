#!/usr/bin/env python3
"""Expose the frozen counter selftest's transport false green; never amend it."""
import argparse
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile

ap = argparse.ArgumentParser()
ap.add_argument('--work', type=pathlib.Path, required=True)
ns = ap.parse_args()
source = pathlib.Path(__file__).with_name('measure88.py')
spec = importlib.util.spec_from_file_location('frozen_counter', source)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='selftest-probe-', dir=ns.work) as directory:
    work = pathlib.Path(directory)
    body = json.dumps({'records': 6, 'findings': [{'id': 'RECORD_ID', 'record': 'R1'}]})
    tool = m.report_partial_tool(work, 'exact-accepted', body)
    packet = work / 'packet.json'
    packet.write_text('{}')
    child = subprocess.run([sys.executable, '-B', str(tool), '--packet', str(packet), '--json'], capture_output=True, text=True)
    suite = subprocess.run([sys.executable, '-B', str(source), '--root', str(source.parents[2]), '--work', str(work), '--selftest'], capture_output=True, text=True)
    result = {'child_rc': child.returncode, 'child_stdout': child.stdout, 'child_stderr': child.stderr,
              'suite_rc': suite.returncode, 'suite_stdout': suite.stdout,
              'false_green': child.returncode != 0 and 'FileNotFoundError' in child.stderr and suite.returncode == 0}
    print(json.dumps(result, indent=2))
    sys.exit(1 if result['false_green'] else 0)
