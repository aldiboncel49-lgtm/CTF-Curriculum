import os
#!/usr/bin/env python3
"""Timing side-channel login oracle (LAB: run this server locally).
The /check endpoint compares your guess to the secret FLAG byte-by-byte and
introduces an artificial delay on each CORRECT byte (early-exit timing leak).
Recover the flag by measuring response times per position.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, urllib.parse

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(q)
        guess = params.get('guess', [''])[0]
        start = time.perf_counter()
        # Early-exit comparison with delay per correct byte (timing leak)
        for i, c in enumerate(guess):
            if i >= len(FLAG) or c != FLAG[i]:
                break
            time.sleep(0.01)  # 10ms per correct byte
        elapsed = time.perf_counter() - start
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"elapsed={elapsed:.4f}".encode())

if __name__ == '__main__':
    print("Run: python3 server.py  (serves on :8000)")
    print("Attack: binary-search each position by timing.")
    HTTPServer(('0.0.0.0', 8000), H).serve_forever()
