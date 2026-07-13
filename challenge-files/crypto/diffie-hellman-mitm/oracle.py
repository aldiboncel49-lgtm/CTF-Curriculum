#!/usr/bin/env python3
"""Diffie-Hellman MITM Challenge"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

# WEAK DH parameters - small prime
p = 23
g = 5

print(f"DH Parameters: p={p}, g={g}")
print("Alice and Bob are exchanging keys. Intercept and decrypt!")
print()

# Simulate Alice
alice_priv = 6
alice_pub = pow(g, alice_priv, p)
print(f"Alice sends: {alice_pub}")

# Simulate Bob  
bob_priv = 15
bob_pub = pow(g, bob_priv, p)
print(f"Bob sends: {bob_pub}")

# Bob encrypts flag with derived key
shared = pow(alice_pub, bob_priv, p)
key = hashlib.sha256(str(shared).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(FLAG.encode(), 16)).hex()
print(f"\nBob sends encrypted flag: {encrypted}")

print("\nYour task: Recover the shared secret and decrypt the flag.")
