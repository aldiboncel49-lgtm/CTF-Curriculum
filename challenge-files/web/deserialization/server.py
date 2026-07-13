import os
#!/usr/bin/env python3
import pickle, base64, os
from http.server import BaseHTTPRequestHandler, HTTPServer

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        try:
            obj = pickle.loads(base64.b64decode(data))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Object processed: " + str(obj).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error: " + str(e).encode())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST a base64-encoded pickle object to /")

if __name__ == '__main__':
    print("FLAG (for solver reference, hidden in source):", FLAG)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
