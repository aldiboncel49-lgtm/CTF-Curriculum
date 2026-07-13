# Challenge Requirements — Environment Setup Guide

Some challenges include ready-to-use target files (HTML pages, binaries, encrypted data). Others require you to set up your own environment. This guide covers what you need for each category.

---

## 🟢 Ready to Solve — Files Included

These challenges come with concrete targets. Download from `challenge-files/` and start immediately:

| Category | Challenges | What You Need |
|---|---|---|
| **Web** (8) | Cookie Monster, Inspector, Header Hunter, Robot's Den, Simple Auth, Directory Buster, Code Viewer, SQL Injection 101 | Python 3 + browser (or `curl`) |
| **Crypto** (8) | Caesar Cipher, Base64 Decode, XOR Basics, RSA Warmup, AES-ECB Oracle, CBC Bit Flipping, FactorDB Attack, Padding Oracle | Python 3 + `pip install pycryptodome` |
| **Pwn** (7) | Buffer Overflow, Format String 0/Write, Integer Overflow, Shellcode Basics, ROP Chain Intro, Heap Overflow | Linux VM (Ubuntu 22.04 recommended), `gdb`, `pwntools` |
| **Reversing** (3) | Simple Check, Strings Analysis, CrackMe | Linux VM, `strings`, `objdump`, `Ghidra` (optional) |
| **Forensics** (3) | Hidden Strings, Magic Bytes, EXIF Data | `strings`, hex editor, `exiftool` |
| **Misc** (3) | QR Code, Esoteric Language, Git History | QR scanner app, Brainfuck interpreter, `git` |

---

## 🟡 Setup Required — Build Your Own Lab

These challenges describe the attack scenario. You must create the vulnerable environment yourself before exploiting it.

### OSINT (8 challenges)

**Requirement:** Internet access + OSINT mindset.

- **Username Search, Email Investigation, Social Graph, Phone Number OSINT** — Search publicly available information online. No tools beyond a browser needed.
- **Image Geolocation, Satellite Imagery** — Use Google Earth, Maps, or satellite imagery platforms.
- **Flight Tracking** — Use public flight tracking websites (FlightRadar24, ADS-B Exchange).
- **Google Dorking** — Use Google search with advanced operators.
- **Dark Web Recon, Cryptocurrency Tracing, APT Attribution** — Use public blockchain explorers, dark web monitoring tools, threat intel platforms.

**No files provided.** The flag is the specific information you discover (format: `CTF{...}`).

---

### Blockchain / Web3 (8 challenges)

**Requirement:** Ethereum testnet access + wallet with test ETH.

- Install [Foundry](https://book.getfoundry.sh/) or [Hardhat](https://hardhat.org/)
- Get testnet ETH from a faucet (Sepolia or Goerli)
- **Beginner:** Deploy the vulnerable contract described in the challenge to testnet, then exploit it
- **Intermediate/Advanced:** Flash loans require a mainnet fork (`anvil --fork-url`)

**No Solidity files provided.** Write the vulnerable contract based on the challenge description, deploy it, then break it.

---

### Cloud (5 challenges)

**Requirement:** AWS free tier account (or equivalent cloud provider).

- **S3 Bucket Exposure** — Create a test S3 bucket with misconfigurations
- **IAM Privilege Escalation** — Set up IAM roles with a privilege escalation path
- **Lambda Event Injection** — Create a Lambda function with a vulnerable event handler
- **Cross-Account AssumeRole** — Configure cross-account roles (two AWS accounts needed)
- **Kubernetes Escape** — Set up a local Kubernetes cluster (`minikube` or `kind`) with a privileged pod

**No Terraform/CloudFormation provided.** Configure the services based on the challenge description.

---

### Network (3 challenges)

**Requirement:** Two VMs on the same virtual network.

- **ARP Spoofing** — Two Linux VMs (VirtualBox/VMware), `arpspoof` from `dsniff` package
- **DNS Poisoning** — VMs + local DNS resolver (`dnsmasq` or `bind9`)
- **BGP Hijack** — Advanced lab with BGP routers (GNS3 or containerlab with FRRouting)

**No VM images provided.** Set up the network topology described in the challenge.

---

### Hardware / IoT (4 challenges)

**Requirement:** Physical or emulated hardware.

- **UART Interface** — Raspberry Pi / Arduino with exposed UART pins, USB-to-TTL adapter
- **SPI Flash Dump** — Router/IoT device + SPI programmer (CH341A)
- **JTAG Debug** — Device with JTAG headers + JTAGulator or FT2232H
- **Side-Channel Power** — ChipWhisperer or oscilloscope + target device
- **Chip Decapping** — Chemical lab equipment (advanced — theoretical challenge)

**No hardware provided.** Physical equipment required for realistic execution.

---

### Mobile (5 challenges)

**Requirement:** Android emulator/device + APK files.

- **APK Decompile** — Download or build an APK matching the challenge description, decompile with `apktool` / `jadx`
- **Insecure Storage** — Android emulator + sample app with `NSUserDefaults` / `SharedPreferences`
- **SSL Pinning Bypass** — Rooted emulator + Frida
- **Root Detection, Biometric Bypass, Deep Link Exploit** — Android emulator + Frida + custom APK

**No APKs provided.** Build a test app matching the challenge scenario, then exploit it.

---

### Pwn Advanced / Expert (5 challenges)

**Requirement:** Linux VM with kernel build capability.

- **Kernel ROP, Heap Feng Shui, ASLR+PIE+Full RELRO, Browser Exploit, VM Escape** — These require compiling custom kernels/modules, building vulnerable drivers, or using specific emulator versions (QEMU, V8 d8 shell).

**No binaries provided.** Follow the challenge description to build the vulnerable component.

---

### Reversing Advanced / Expert (5 challenges)

**Requirement:** Binary samples (build yourself or find matching scenarios).

- **Packed Binary** — Use UPX or custom packer on any simple C binary, then analyze
- **Anti-Debugging** — Build a binary with `ptrace` anti-debug, then bypass
- **Obfuscated JavaScript** — Write a JS obfuscator or use existing obfuscated samples
- **Go Binary, OLLVM, VM-based Obfuscation, Kernel Driver, Firmware Backdoor** — Build matching binaries based on challenge description

**No binaries provided.** Build the obfuscated/packed/protected binary first.

---

### Forensics Advanced / Expert (5 challenges)

**Requirement:** Disk images, memory dumps, or specialized captures.

- **Memory Dump, NTFS Journal, APT C2 Traffic, Ransomware Analysis, CPU Side Channel, Firmware Extraction** — These require specific datasets (memory dumps from Volatility samples, PCAP from malware-traffic-analysis.net, firmware from vendor sites, etc.)

**No files provided.** Source sample datasets from public repositories matching the challenge scenario.

---

### Crypto Theory (8 challenges)

**Requirement:** Paper + pen or Python with `sage`/`pycryptodome`.

- **Diffie-Hellman MITM, Hash Length Extension, Wiener's Attack, Bleichenbacher, Lattice Attack, Boneh-Durfee, S-box Differential Cryptanalysis** — These are purely mathematical. Write the solver script yourself based on the cryptanalysis technique described.

**No oracle scripts provided.** Implement the attack from scratch based on the challenge description.

---

## Summary

| Type | Count | Status |
|---|---|---|
| 🟢 **Ready files provided** | 26 | Download → solve |
| 🟡 **Setup required** | 116 | Build lab → solve |

**Flag format for all challenges:** `CTF{...}`

---

## Minimum Toolset

Install these once to cover most challenges:

```bash
# Python fundamentals
pip install requests pycryptodome pwntools frida-tools

# Binary analysis
sudo apt install binutils gdb strings exiftool

# Web
sudo apt install curl wget

# Blockchain
curl -L https://foundry.paradigm.xyz | bash

# Network
sudo apt install dsniff dnsmasq wireshark