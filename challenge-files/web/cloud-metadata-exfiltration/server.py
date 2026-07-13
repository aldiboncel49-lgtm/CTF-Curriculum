import os
#!/usr/bin/env python3
"""SSRF -> cloud metadata (169.254.169.254) exfiltration.
The app fetches a user-supplied URL. Use it to hit the link-local metadata endpoint.
"""
from flask import Flask, request
import urllib.request
app = Flask(__name__)
@app.route('/fetch')
def fetch():
    url = request.args.get('url','')
    # VULN: no SSRF filter -> can reach 169.254.169.254
    try:
        data = urllib.request.urlopen(url, timeout=3).read().decode()
    except Exception as e:
        return f"error: {e}"
    return data
@app.route('/flag')
def flag():
    return os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")
if __name__ == '__main__':
    app.run(port=5006)
