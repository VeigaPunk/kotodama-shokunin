#!/usr/bin/env python3
"""Twenty loopback ports, one real host, ordinary GETs. No counter transport shim."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
import time

parser = argparse.ArgumentParser()
parser.add_argument('--ready', required=True)
parser.add_argument('--log', required=True)
parser.add_argument('--case', required=True)
args = parser.parse_args()
log_lock = threading.Lock()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/leaf':
            i = self.server.fixture_index
            text = (f'<html><head><title>Object catalogue</title></head><body><p>The amulet was carried by the household '
                    f'as a protective charm during ceremony number {i}.</p>'
                    '<p>Amulets were worn in ceremonies and talismans were placed above thresholds. '
                    'The protective charm was made for ritual protection.</p></body></html>')
        else:
            text = '<html><body>Welcome to the museum. Contact and opening hours.</body></html>'
        body = text.encode()
        record = {'case': Path(args.case).read_text().strip(), 'method': 'GET', 'status': 200,
                  'url': 'http://' + self.headers['Host'] + self.path}
        with log_lock:
            with open(args.log, 'a', encoding='utf-8') as handle:
                handle.write(json.dumps(record) + '\n')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, format, *args):
        pass

Path(args.log).write_text('')
servers = []
for i in range(20):
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    server.fixture_index = i
    servers.append(server)
    threading.Thread(target=server.serve_forever, daemon=True).start()
Path(args.ready).write_text(json.dumps({'ports': [server.server_address[1] for server in servers]}))
while True:
    time.sleep(60)
