import os
#!/usr/bin/env python3
"""Flawed Schnorr-like ZK proof of knowledge of discrete log.
The verifier accepts a proof where the prover's response r = (k - c*x) mod q.
FLAW: the challenge c is reused / predictable, allowing secret x recovery.
Recover x (the secret) and derive the flag.
"""
from Crypto.Util.number import getPrime, long_to_bytes
import random

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF  # secp256k1 prime
q = (p + 1) // 4
g = 2
x = random.getrandbits(256)  # SECRET
X = pow(g, x, p)  # public key

# Flawed proof: prover sends (k, r) where r = k - c*x, but c is FIXED = 1
c = 1
k = random.getrandbits(256)
r = (k - c * x) % q

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]").encode()
ct = pow(int.from_bytes(FLAG, 'big'), 65537, p)

if __name__ == '__main__':
    print(f"p = {p}")
    print(f"g = {g}")
    print(f"X (public key) = {X}")
    print(f"k = {k}")
    print(f"r (response) = {r}")
    print(f"c (challenge) = {c}")
    print(f"ciphertext = {ct}")
    print("\nRecover x from r = k - c*x (mod q) with known k, r, c=1.")
    print("Then x = (k - r) * inverse(c, q) mod q. Flag = pow(ciphertext, d, p).")
