import os
#!/usr/bin/env python3
"""Lattice-based attack on biased LCG (hidden number problem variant).
Recover the seed from biased outputs using LLL.
"""
from Crypto.Util.number import long_to_bytes

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]").encode()

# LCG with known parameters but biased high bits leaked
m = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # 128-bit modulus
a = 0x5851F42D4C957F2D
c = 0x14057B7EF767814F
seed = int.from_bytes(FLAG.ljust(16, b'\x00'), 'big')

# Generate outputs but only reveal top 40 bits (leak)
outputs = []
state = seed
for _ in range(20):
    state = (a * state + c) % m
    # Leak: top 40 bits of state
    leak = state >> (128 - 40)
    outputs.append(leak)

if __name__ == '__main__':
    print("Modulus m =", m)
    print("Multiplier a =", hex(a))
    print("Increment c =", hex(c))
    print("Leaked top 40 bits of 20 consecutive states:")
    for i, o in enumerate(outputs):
        print(f"  state[{i}] top40 = {o}")
    print("\nRecover seed via lattice reduction (LLL/Coppersmith).")
    print("Flag is the original seed as bytes.")
