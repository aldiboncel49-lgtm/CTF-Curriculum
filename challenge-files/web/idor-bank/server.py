import os
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Accounts database - flag is in victim's account
ACCOUNTS = {
    "1001": {"owner": "attacker", "balance": 50, "note": "your account"},
    "1002": {"owner": "victim", "balance": 99999, "note": os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")},
}
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Vulnerable: reads account by ID from query without auth check
        if '/api/account?' in self.path:
            acc_id = self.path.split('id=')[1].split('&')[0]
            if acc_id in ACCOUNTS:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(ACCOUNTS[acc_id]).encode())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"GET /api/account?id=XXXX")

if __name__ == '__main__':
    print("FLAG:", FLAG)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
