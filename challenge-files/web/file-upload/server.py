#!/usr/bin/env python3
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

ALLOWED = ['.jpg', '.png', '.gif']

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Vulnerable: only checks extension, not content
        fn = self.headers.get('X-Filename', 'upload.bin')
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        if os.path.splitext(fn)[1] in ALLOWED:
            with open(os.path.join(UPLOAD_DIR, fn), 'wb') as f:
                f.write(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Uploaded: " + fn.encode())
        else:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"File type not allowed")

if __name__ == '__main__':
    print("FLAG:", FLAG)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
