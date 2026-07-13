Vulnerable kernel module (vuln_module.c) with an unchecked copy_from_user.
Build, load on a test VM, then craft a kernel ROP chain via the ioctl.
harness.py models the contract for exploit prototyping.
