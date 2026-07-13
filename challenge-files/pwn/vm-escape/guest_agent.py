#!/usr/bin/env python3
"""VM-escape challenge: a guest-agent shared-memory service (LAB).
The host exposes a shared memory region; the guest agent can write to it.
VULN: the agent can map BEYOND its allocated region (no bounds check),
allowing escape into host memory where the flag lives.
"""
import mmap, os, struct

SHM_PATH = '/dev/shm/vm_escape_shm'
HOST_FLAG_OFFSET = 0x1000  # beyond guest region

def guest_write(payload):
    # Open shared mem (guest region is 0x0..0xFFF)
    fd = os.open(SHM_PATH, os.O_RDWR)
    mm = mmap.mmap(fd, 0x2000, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
    # VULN: no bounds check, can write at HOST_FLAG_OFFSET
    mm[HOST_FLAG_OFFSET:HOST_FLAG_OFFSET+len(payload)] = payload
    mm.close(); os.close(fd)

if __name__ == '__main__':
    print("Guest agent can write beyond its region. Escape to host memory at offset 0x1000.")
    print("The flag is stored by the host at that offset.")
