#!/usr/bin/env python3
"""AES-ECB Oracle Challenge"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")
KEY = os.urandom(16)

def encrypt(user_input):
    """Encrypts user_input + FLAG with AES-ECB"""
    cipher = AES.new(KEY, AES.MODE_ECB)
    data = user_input.encode() + FLAG.encode()
    return cipher.encrypt(pad(data, 16)).hex()

if __name__ == '__main__':
    print("AES-ECB Oracle")
    print("Send any text and I'll encrypt it together with the flag.")
    print("Type 'quit' to exit.")
    while True:
        inp = input("> ")
        if inp == 'quit': break
        print(encrypt(inp))
