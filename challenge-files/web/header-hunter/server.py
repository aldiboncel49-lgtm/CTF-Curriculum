#!/usr/bin/env python3
"""Header Hunter - serves flag in custom HTTP header"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class HeaderHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Flag', os.environ.get('CTF_FLAG', '[SET_CTF_FLAG_TO_SOLVE]'))
        self.send_header('X-Hint', 'Check your response headers carefully')
        super().end_headers()
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    HTTPServer(('127.0.0.1', 8080), HeaderHandler).serve_forever()
