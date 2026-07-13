#!/usr/bin/env python3
"""Bleichenbacher's PKCS#1 v1.5 padding oracle attack challenge.
The oracle tells you if a ciphertext decrypts to a PKCS#1 v1.5 compliant plaintext.
"""
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]").encode()

key = RSA.generate(2048)
n = key.n
e = key.e
d = key.d

# Encrypt flag with PKCS1 v1.5
from Crypto.Util.number import bytes_to_long
# PKCS1 v1.5 padding: 0x00 0x02 [non-zero random] 0x00 [message]
pad_len = 256 - 3 - len(FLAG)
padding = b'\x00\x02' + os.urandom(pad_len).replace(b'\x00', b'\x01') + b'\x00' + FLAG
m = bytes_to_long(padding)
c = pow(m, e, n)

def oracle(ciphertext_int):
    """Returns True if decryption has valid PKCS#1 v1.5 prefix"""
    mm = pow(ciphertext_int, d, n)
    dec = long_to_bytes(mm, 256)
    if len(dec) < 2: return False
    if dec[0] != 0x00 or dec[1] != 0x02:
        return False
    # Check for 0x00 separator
    if b'\x00' in dec[2:]:
        return True
    return False

if __name__ == '__main__':
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"ciphertext = {c}")
    print("\nUse the oracle() function to perform Bleichenbacher's attack.")
    print("The flag is in the decrypted PKCS#1 v1.5 message.")
