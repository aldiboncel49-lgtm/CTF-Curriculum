# CTF Challenge Curriculum — Pure Challenge Repository

**142 standalone CTF challenges** across 12 categories, organized by difficulty tier.

No writeups. No hints. No source references. Just the challenge description and your skills.

---

## Difficulty Tiers

| Tier | Name | Description |
|---|---|---|
| **01** | 🌱 Beginner | Fundamentals — basic tools, pattern recognition, single-step solutions |
| **02** | ⚔️ Intermediate | Technique chaining — multiple steps, category-specific tools |
| **03** | 💀 Advanced | Complex exploitation — custom tools, novel attack paths |
| **04** | 🔥 Expert | Research-level — zero-day territory, cross-domain attacks |

---

## Categories (12)

| # | Category | Challenges |
|---|---|---|
| **01** | Web | SQLi, XSS, CSRF, SSRF, SSTI, Deserialization, Request Smuggling, more |
| **02** | Pwn / Binary Exploitation | Stack overflow, ROP, format string, heap, kernel, browser |
| **03** | Cryptography | Classical ciphers, RSA, AES, padding oracle, lattice, ECC |
| **04** | Reverse Engineering | Disassembly, unpacking, anti-debug, VM-based obfuscation |
| **05** | Forensics | File carving, memory forensics, steganography, PCAP analysis |
| **06** | OSINT | Username search, geolocation, satellite imagery, dark web |
| **07** | Blockchain / Web3 | Reentrancy, flash loans, oracles, governance, cross-chain |
| **08** | Mobile | APK decompile, SSL pinning bypass, Frida, deep links |
| **09** | Hardware / IoT | UART, JTAG, SPI flash dump, side-channel, firmware |
| **10** | Cloud | S3 bucket exposure, IAM escalation, Lambda injection, K8s escape |
| **11** | Network | ARP spoofing, DNS poisoning, BGP hijack |
| **12** | Misc / Programming | Esoteric languages, polyglot files, protocol reverse, ZK proofs |

---

## Repository Structure

```
CTF-Curriculum/
├── 01-beginner/          🌱 Fundamentals
│   ├── web/              (7 challenges)
│   ├── pwn/              (5 challenges)
│   ├── crypto/           (5 challenges)
│   ├── reversing/        (4 challenges)
│   ├── forensics/        (5 challenges)
│   ├── osint/            (4 challenges)
│   ├── blockchain/       (4 challenges)
│   ├── mobile/           (2 challenges)
│   ├── hardware/         (1 challenge)
│   ├── network/          (1 challenge)
│   └── misc/             (5 challenges)
│
├── 02-intermediate/      ⚔️ Technique chaining
│   ├── web/              (9 challenges)
│   ├── pwn/              (5 challenges)
│   ├── crypto/           (5 challenges)
│   ├── reversing/        (4 challenges)
│   ├── forensics/        (4 challenges)
│   ├── osint/            (4 challenges)
│   ├── blockchain/       (4 challenges)
│   ├── mobile/           (2 challenges)
│   ├── hardware/         (2 challenges)
│   ├── cloud/            (2 challenges)
│   ├── network/          (2 challenges)
│   └── misc/             (4 challenges)
│
├── 03-advanced/          💀 Deep exploitation
│   ├── web/              (6 challenges)
│   ├── pwn/              (3 challenges)
│   ├── crypto/           (4 challenges)
│   ├── reversing/        (3 challenges)
│   ├── forensics/        (3 challenges)
│   ├── osint/            (3 challenges)
│   ├── blockchain/       (3 challenges)
│   ├── mobile/           (2 challenges)
│   ├── hardware/         (1 challenge)
│   ├── cloud/            (2 challenges)
│   ├── network/          (1 challenge)
│   └── misc/             (2 challenges)
│
└── 04-expert/            🔥 Research-level
    ├── web/              (3 challenges)
    ├── pwn/              (2 challenges)
    ├── crypto/           (2 challenges)
    ├── reversing/        (2 challenges)
    ├── forensics/        (2 challenges)
    ├── osint/            (1 challenge)
    ├── blockchain/       (1 challenge)
    ├── mobile/           (1 challenge)
    ├── hardware/         (1 challenge)
    ├── cloud/            (1 challenge)
    └── misc/             (2 challenges)
```

---

## How to Use

1. **Pick a category** — choose what you want to practice
2. **Start at your level** — beginner if new, higher if experienced
3. **Solve the challenge** — read the description, find the flag
4. **No hints provided** — you must figure it out yourself

Each challenge directory contains a single `challenge.md` file with:
- Challenge name
- Category and difficulty
- Description of the problem
- Objective (find the flag)

**That's it.** No references, no writeups, no source attribution.