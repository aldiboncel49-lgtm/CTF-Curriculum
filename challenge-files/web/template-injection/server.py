import os
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from string import Template

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if 'name=' in self.path:
            name = self.path.split('name=')[1].split('&')[0]
            # Vulnerable: user input directly in template
            t = Template("Hello $name")
            try:
                result = t.substitute(name=name)
            except Exception as e:
                # Fallback: dangerous eval-like
                result = "Hello " + name
            self.send_response(200)
            self.end_headers()
            self.wfile.write(result.encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"GET /?name=YOUR_INPUT")

if __name__ == '__main__':
    print("FLAG:", FLAG)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
