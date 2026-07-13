import os
#!/usr/bin/env python3
"""Race condition: balance transfer. Send concurrent requests to go negative / double-spend.
"""
from flask import Flask, request, jsonify
import threading
app = Flask(__name__)
bal = {'alice': 100}
lock = threading.Lock()

@app.route('/transfer', methods=['POST'])
def transfer():
    amt = int(request.json.get('amount', 0))
    # VULN: check and act are not atomic -> race window
    if bal['alice'] >= amt:           # CHECK
        # (race window here)
        bal['alice'] -= amt           # ACT
        return jsonify({'ok':True,'bal':bal['alice']})
    return jsonify({'ok':False,'bal':bal['alice']}), 400

@app.route('/flag')
def flag():
    # Flag appears once balance goes below 0 (exploited) OR accumulates 1000+
    if bal['alice'] < 0 or bal['alice'] >= 1000:
        return os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")
    return "keep racing"

if __name__ == '__main__':
    app.run(threaded=True, port=5001)
