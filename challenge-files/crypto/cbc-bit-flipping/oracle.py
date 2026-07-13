#!/usr/bin/env python3
"""CBC Bit Flipping Challenge"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

KEY = os.urandom(16)
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

def create_cookie():
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    cookie = f"username=guest&admin=false&flag=REDACTED"
    ct = cipher.encrypt(pad(cookie.encode(), 16))
    return (iv + ct).hex()

def check_cookie(hex_cookie):
    try:
        data = bytes.fromhex(hex_cookie)
        iv, ct = data[:16], data[16:]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), 16).decode()
        print(f"Decrypted cookie: {pt}")
        if "admin=true" in pt:
            print(f"SUCCESS! Flag: {FLAG}")
        else:
            print("Not admin. Access denied.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    cookie = create_cookie()
    print(f"Your cookie (hex): {cookie}")
    print("\nModify this cookie to become admin!")
    print("Enter modified cookie (hex) or 'quit':")
    while True:
        inp = input("> ")
        if inp == 'quit': break
        check_cookie(inp)
