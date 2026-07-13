#!/usr/bin/env python3
import os, base64, json
PLACEHOLDER = "[SET_CTF_FLAG_TO_SOLVE]"

def b64d(s):
    return base64.urlsafe_b64decode(s + '=' * (-len(s) % 4))

def verify(token):
    parts = token.split('.')
    if len(parts) != 3:
        return None
    h = b64d(parts[0])
    if b'"alg":"none"' in h:           # VULNERABLE: accepts alg=none
        try:
            return json.loads(b64d(parts[1]))
        except Exception:
            return None
    return None

if __name__ == '__main__':
    import os
    tok_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'token.txt')
    tok = open(tok_path).read().strip()
    p = verify(tok)
    if p and p.get('admin') is True:
        print("FLAG:", os.environ.get("CTF_FLAG", PLACEHOLDER))
    else:
        print("Current token is not admin. Forge a token with alg=none and admin=true to get the flag.")
