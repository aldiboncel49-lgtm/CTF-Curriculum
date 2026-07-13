import os
#!/usr/bin/env python3
"""NoSQL-style injection login (uses an in-memory "DB", no Mongo needed).
The login handler does a direct dict lookup: db.find({'username':u,'password':p}).
Send a JSON body with operator objects to bypass auth.
"""
from flask import Flask, request, jsonify
app = Flask(__name__)

USERS = [{'username':'admin','password':'s3cr3t','flag': os.environ.get('CTF_FLAG', '[SET_CTF_FLAG_TO_SOLVE]')}]

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json(force=True, silent=True) or {}
    u = body.get('username')
    p = body.get('password')
    # VULN: body values can be dicts like {"$gt":""} -> Mongo-style operator
    for user in USERS:
        if user['username'] == u and user['password'] == p:
            return jsonify({'ok':True,'flag':user['flag']})
    return jsonify({'ok':False}), 401

if __name__ == '__main__':
    app.run(port=5000)
