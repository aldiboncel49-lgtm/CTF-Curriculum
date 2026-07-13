#!/usr/bin/env python3
"""Cache poisoning: an unkeyed header is reflected into the cached response."""
import os
from flask import Flask, request
app = Flask(__name__)
PLACEHOLDER = "[SET_CTF_FLAG_TO_SOLVE]"
FLAG = os.environ.get("CTF_FLAG", PLACEHOLDER)
CACHE = {}

@app.route('/')
def index():
    # VULN: X-Forwarded-Host (unkeyed) is reflected into a cached asset URL
    host = request.headers.get('X-Forwarded-Host', 'safe.example.com')
    body = f'<script src="https://{host}/evil.js"></script>'
    if 'poisoned' in CACHE:
        cached = CACHE['poisoned']
        # VULN achieved: attacker-controlled host was cached
        if 'evil.js' in cached:
            return cached + f" <!-- FLAG: {FLAG} -->"
        return cached
    CACHE['poisoned'] = body  # first request wins the cache
    return body

if __name__ == '__main__':
    app.run(port=5002)
