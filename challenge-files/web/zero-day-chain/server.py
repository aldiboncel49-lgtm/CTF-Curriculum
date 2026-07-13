import os
#!/usr/bin/env python3
"""Zero-day chain: auth bypass (JWT alg=none) + SSTI in a report field.
"""
from flask import Flask, request, render_template_string
import base64, json
app = Flask(__name__)
SECRET = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")
@app.route('/report', methods=['POST'])
def report():
    token = request.headers.get('X-Token','')
    # VULN 1: alg=none accepted
    try:
        payload = json.loads(base64.urlsafe_b64decode(token.split('.')[1]+'==='))
    except: payload = {}
    if payload.get('role') != 'admin':
        return "denied", 403
    # VULN 2: SSTI in template
    tpl = request.json.get('template','')
    return render_template_string(tpl)  # SSTI -> {{7*7}}
@app.route('/flag')
def flag():
    return SECRET
if __name__ == '__main__':
    app.run(port=5005)
