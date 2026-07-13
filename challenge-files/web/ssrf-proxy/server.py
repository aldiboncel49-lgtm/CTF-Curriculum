import os
#!/usr/bin/env python3
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

# Internal admin panel at http://127.0.0.1:8080/admin has the flag
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if 'url=' in self.path:
            url = self.path.split('url=')[1].split('&')[0]
            try:
                resp = urllib.request.urlopen(url, timeout=5)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(resp.read()[:500])
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Fetch failed: " + str(e).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"GET /?url=http://TARGET")

if __name__ == '__main__':
    print("FLAG:", FLAG)
    print("Hint: Internal admin at http://127.0.0.1:8080/admin")
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
