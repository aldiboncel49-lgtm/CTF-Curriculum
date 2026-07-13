import os
#!/usr/bin/env python3
"""Boneh-Durfee (Coppersmith) small-d attack.
Recover d from (n, e) where d < N^0.292.
Run this to print n, e, and the ciphertext. Implement the lattice attack to recover d.
"""
from Crypto.Util.number import getPrime, inverse, long_to_bytes

p = getPrime(512)
q = getPrime(512)
n = p * q
import random
random.seed(0x5EED)
# Construct a small d (~256 bits, well below N^0.292 ~ 300 bits)
d = random.getrandbits(255) | (1 << 254)
phi = (p-1)*(q-1)
e = inverse(d, phi)
assert (e * d) % phi == 1

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]").encode()
ct = pow(int.from_bytes(FLAG, 'big'), e, n)

if __name__ == '__main__':
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"ciphertext = {ct}")
    print("\nUse Boneh-Durfee lattice reduction (LLL) to recover d, then decrypt:")
    print("m = pow(ciphertext, d, n); flag = long_to_bytes(m)")
