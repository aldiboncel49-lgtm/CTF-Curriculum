import os
#!/usr/bin/env python3
"""SQL Injection 101 - vulnerable login page"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3, os, urllib.parse

class SQLiHandler(BaseHTTPRequestHandler):
    def setup_db(self):
        self.conn = sqlite3.connect(':memory:')
        c = self.conn.cursor()
        c.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
        c.execute("INSERT INTO users VALUES (1, 'admin', 'supersecretpassword123')")
        c.execute("INSERT INTO users VALUES (2, 'user', 'password')")
        # The flag table
        c.execute("CREATE TABLE flags (id INTEGER, flag TEXT)")
        c.execute("INSERT INTO flags VALUES (1, os.environ.get('CTF_FLAG', '[SET_CTF_FLAG_TO_SOLVE]'))")
        self.conn.commit()
    
    def do_GET(self):
        if self.path == '/':
            self.serve_file('index.html')
        elif self.path == '/login':
            self.serve_file('login.html')
        else:
            self.send_response(404); self.end_headers()
    
    def do_POST(self):
        if self.path == '/login':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode()
            params = urllib.parse.parse_qs(body)
            username = params.get('username', [''])[0]
            password = params.get('password', [''])[0]
            
            # VULNERABLE: string concatenation SQL
            self.setup_db()
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            try:
                c = self.conn.cursor()
                c.execute(query)
                user = c.fetchone()
                if user:
                    c.execute("SELECT flag FROM flags WHERE id=1")
                    flag_row = c.fetchone()
                    flag = flag_row[0] if flag_row else "FLAG_NOT_FOUND"
                    self.send_json({"status": "success", "message": f"Login successful!", "flag": flag})
                else:
                    self.send_json({"status": "error", "message": "Invalid credentials"})
            except Exception as e:
                self.send_json({"status": "error", "message": str(e)})
        else:
            self.send_response(404); self.end_headers()
    
    def serve_file(self, filename):
        path = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(path):
            with open(path) as f: content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
    
    def send_json(self, data):
        import json
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    HTTPServer(('127.0.0.1', 8081), SQLiHandler).serve_forever()
