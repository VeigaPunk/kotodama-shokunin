#!/usr/bin/env python3
"""Deterministic public-protocol fixture, served only on loopback using http.server."""
import argparse
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import re
import threading
import time
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument('--ready', required=True)
parser.add_argument('--log', required=True)
args = parser.parse_args()
counts = Counter()
lock = threading.Lock()

GAP_QUOTE = 'The stone was catalogued in a quiet museum before readers discussed protective history.'

def quote(index=0):
    return f'The amulet was carried by the household as a protective charm during ceremony number {index}.'

def page(index=0, gap=False):
    paragraph = GAP_QUOTE if gap else quote(index)
    return ('<html><head><title>Object catalogue</title></head><body><p>' + paragraph + '</p>'
            '<p>Amulets were worn in ceremonies and talismans were placed above thresholds. '
            'The protective charm was made for ritual protection.</p></body></html>').encode()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        canonical = self.headers.get('X-Fixture-URL', '')
        tag = self.headers.get('X-Fixture-Run', '')
        if self.path == '/events':
            with lock:
                rows = [json.loads(line) for line in open(args.log, encoding='utf-8')]
            body = json.dumps(rows).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        parts = urllib.parse.urlsplit(canonical)
        archived = parts.netloc == 'web.archive.org'
        stamp = None
        if archived:
            match = re.match(r'^/web/(\d+)[a-z_]*/(https?://.*)$', parts.path)
            if not match:
                self.send_error(400)
                return
            stamp = match.group(1)
            original = urllib.parse.urlsplit(match.group(2))
        else:
            original = parts
        host = original.hostname or ''
        path = original.path or '/'
        with lock:
            counts[(tag, canonical)] += 1
            attempt = counts[(tag, canonical)]
        status = 200
        body = b'<html><body>Welcome to the museum. Contact and opening hours.</body></html>'
        is_root = path == '/'
        if not is_root:
            index_match = re.search(r'(?:good|positive)(\d+)', host)
            index = int(index_match.group(1)) if index_match else 0
            body = page(index, gap=host.startswith('topicgap'))
        if not archived and host.startswith('deny403'):
            status = 403
        elif not archived and host.startswith('deny404'):
            status = 404
        elif is_root and host.startswith(('root403', 'rootsfail')) and not archived:
            status = 403
        elif is_root and host.startswith('rootsfail') and archived:
            status = 403
        elif not is_root and host.startswith('transient429') and attempt == 1:
            status = 429
        elif not is_root and host.startswith('always429'):
            status = 429
        elif not is_root and host.startswith('transient501') and attempt == 1:
            status = 501
        if host.startswith('race'):
            time.sleep(0.25)
        if status != 200:
            body = f'Fixture HTTP {status}'.encode()
        event = {'run': tag, 'method': 'GET', 'url': canonical, 'status': status,
                 'attempt': attempt, 'archive_timestamp': stamp}
        with lock:
            with open(args.log, 'a', encoding='utf-8') as handle:
                handle.write(json.dumps(event) + '\n')
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Retry-After', '0')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

open(args.log, 'w', encoding='utf-8').close()
server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
with open(args.ready, 'w', encoding='utf-8') as handle:
    json.dump({'port': server.server_address[1]}, handle)
server.serve_forever()
