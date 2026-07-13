#!/usr/bin/env python3
"""SIMULATED ransomware for analysis (educational, no real harm).
It encrypts a victim file with AES-CTR using a derived key.
Your job: analyze this script, recover the key, and decrypt victim.enc.
"""
from Crypto.Cipher import AES
from Crypto.Util import Counter

KEY = b"r4ns0m_k3y_4n4ly"  # 16 bytes
NONCE = b"\x00" * 8

def encrypt(data):
    ctr = Counter.new(64, prefix=NONCE)
    return AES.new(KEY, AES.MODE_CTR, counter=ctr).encrypt(data)

if __name__ == '__main__':
    import sys
    data = open(sys.argv[1], 'rb').read()
    open(sys.argv[1] + '.enc', 'wb').write(encrypt(data))
    print("File encrypted (simulated).")
