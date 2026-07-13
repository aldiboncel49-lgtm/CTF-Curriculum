#!/usr/bin/env python3
"""Userland harness mimicking the kernel driver ioctl verify_key() logic.
Reverse this to recover the key, or load driver.c on a test kernel.
"""
def verify_key(key):
    target = "[REDACTED]"
    for i in range(len(target)):
        if (ord(key[i]) ^ 0xAA) != ord(target[i]):
            return False
    return True

if __name__ == '__main__':
    import sys
    k = sys.argv[1] if len(sys.argv) > 1 else "[REDACTED]"
    print("OK" if verify_key(k) else "FAIL")
