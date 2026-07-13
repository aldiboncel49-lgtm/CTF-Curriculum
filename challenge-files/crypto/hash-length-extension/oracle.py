#!/usr/bin/env python3
"""Hash Length Extension Challenge"""
import hashlib
import os

SECRET = os.urandom(16)
FLAG = os.environ.get("CTF_FLAG", "[SET_CTF_FLAG_TO_SOLVE]")

def create_mac(message):
    """MAC = SHA256(secret || message)"""
    return hashlib.sha256(SECRET + message).hexdigest()

def verify_mac(message, mac):
    """Check if MAC matches"""
    expected = hashlib.sha256(SECRET + message).hexdigest()
    return expected == mac

if __name__ == '__main__':
    original_msg = b"user=guest"
    original_mac = create_mac(original_msg)
    
    print(f"Original message: {original_msg.decode()}")
    print(f"MAC: {original_mac}")
    print(f"\nYour task: Append '&admin=true' to the message without knowing the secret.")
    print("Provide a new message (hex) and MAC (hex):")
    
    while True:
        try:
            msg_hex = input("Message (hex): ").strip()
            mac_hex = input("MAC (hex): ").strip()
            msg = bytes.fromhex(msg_hex)
            
            if verify_mac(msg, mac_hex):
                if b"admin=true" in msg:
                    print(f"SUCCESS! Flag: {FLAG}")
                else:
                    print("MAC valid but message is still guest.")
            else:
                print("Invalid MAC!")
        except Exception as e:
            print(f"Error: {e}")
        print()
