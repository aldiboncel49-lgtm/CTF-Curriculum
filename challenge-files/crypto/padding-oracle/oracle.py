#!/usr/bin/env python3
"""Padding Oracle Challenge"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

KEY = os.urandom(16)
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

def encrypt_flag():
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(FLAG.encode(), 16))
    return (iv + ct).hex()

def check_padding(hex_data):
    """Returns True if padding is valid, False otherwise"""
    try:
        data = bytes.fromhex(hex_data)
        iv, ct = data[:16], data[16:]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), 16)
        return True
    except:
        return False

if __name__ == '__main__':
    ct_hex = encrypt_flag()
    print(f"Encrypted flag: {ct_hex}")
    print("\nPadding Oracle - send IV+CT in hex, I'll tell you if padding is valid.")
    print("Type 'quit' to exit.")
    while True:
        inp = input("> ")
        if inp == 'quit': break
        valid = check_padding(inp)
        print(f"Padding valid: {valid}")
