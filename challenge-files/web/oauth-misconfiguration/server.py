import os
#!/usr/bin/env python3
"""OAuth misconfig: state parameter not validated + open redirect on callback.
"""
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route('/oauth/callback')
def cb():
    # VULN: 'state' not checked; 'redirect_uri' accepts any host (open redirect)
    code = request.args.get('code')
    redir = request.args.get('redirect_uri', '/')
    # Attacker can force redir to their site carrying the code
    return redirect(redir + '?code=' + (code or ''))
@app.route('/flag')
def flag():
    return os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")
if __name__ == '__main__':
    app.run(port=5003)
