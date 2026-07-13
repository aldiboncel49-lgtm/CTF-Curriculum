#!/usr/bin/env python3
"""Simple 4-round SPN cipher (16-bit block, 4-bit S-boxes).
Recover the 16-bit master key via differential cryptanalysis.
The key is UNKNOWN. Use the 2000 PT/CT pairs in pairs.txt.
This file gives you the cipher so you can verify candidate keys:
    assert encrypt(pt, candidate) == ct  for all pairs.
"""
SBOX = [0xE,0x4,0xD,0x1,0x2,0xF,0xB,0x8,0x3,0xA,0x6,0xC,0x5,0x9,0x0,0x7]
P = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]

def sbox_layer(x):
    out = 0
    for i in range(4):
        out |= SBOX[(x >> (4*i)) & 0xF] << (4*i)
    return out

def perm_layer(x):
    out = 0
    for i in range(16):
        if (x >> i) & 1:
            out |= 1 << P[i]
    return out

def round_keys(master):
    rk = [master & 0xFFFF]
    for _ in range(3):
        rk.append(((rk[-1] << 3) ^ 0x1234) & 0xFFFF)
    return rk

def encrypt(pt, master):
    rk = round_keys(master)
    x = pt ^ rk[0]
    for r in range(3):
        x = sbox_layer(x)
        x = perm_layer(x)
        x ^= rk[r+1]
    x = sbox_layer(x)
    x ^= rk[3]
    return x

if __name__ == '__main__':
    # Example verification against pairs.txt
    import sys
    if len(sys.argv) > 1:
        cand = int(sys.argv[1], 16)
        ok = 0
        total = 0
        for line in open('pairs.txt'):
            if line.startswith('#'): continue
            pt, ct = (int(v,16) for v in line.strip().split(','))
            total += 1
            if encrypt(pt, cand) == ct:
                ok += 1
        print(f"Key {cand:04X}: {ok}/{total} pairs match")
