#!/usr/bin/env python3
"""Request smuggling demo: server reads Content-Length but a front proxy uses
Transfer-Encoding. The ambiguity lets an attacker prefix a hidden request.
This is a SIMULATED handler that splits requests the way a desync would."""
import os
from flask import Flask, request
app = Flask(__name__)
PLACEHOLDER = "[SET_CTF_FLAG_TO_SOLVE]"
FLAG = os.environ.get("CTF_FLAG", PLACEHOLDER)
CRLF = "\r\n\r\n"

@app.route('/', methods=['POST'])
def handler():
    raw = request.get_data(as_text=True)
    if CRLF in raw:
        head, _, tail = raw.partition(CRLF)
        # VULN: tail is treated as a separate smuggled request
        if 'admin=1' in tail or 'admin=true' in tail:
            return f"smuggled admin request executed. FLAG: {FLAG}"
        return f"processed: [{head[:40]}] smuggled: [{tail[:40]}]"
    return f"processed: [{raw[:40]}]"

if __name__ == '__main__':
    app.run(port=5004)
