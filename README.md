# CyberSec & Systems Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Primary-Rust-orange?style=flat-square&logo=rust" alt="Rust" />
  <img src="https://img.shields.io/badge/Focus-Low--Level%20Security%20%26%20Linux%20Tooling-red?style=flat-square&logo=linux" alt="Focus" />
  <img src="https://img.shields.io/badge/Secondary-Python%20%7C%20Java%20%7C%20Bash-blue?style=flat-square" alt="Languages" />
  <img src="https://img.shields.io/badge/OS-Linux%20%28Arch--based%2FCachyOS%29-lightgrey?style=flat-square&logo=archlinux" alt="OS" />
</p>

Welcome to my cybersecurity and systems engineering portfolio. This repository documents my hands-on security research, CTF writeups, automation tooling, and low-level Linux projects.

---

## Primary Language: RUST

Rust is my primary language for systems programming, low-level binary inspection, and security tooling. I build high-performance, memory-safe utilities in Rust, supported by Python, Java, and Bash for scripting and secondary tooling.

---

## About Me

I'm obsessed with figuring out how software works under the hood. Most of my time is spent digging into low-level binaries, finding security flaws, and building fast tools for Linux.

- **Creator** at [**briDge**](https://github.com/brRige) — Building open-source Linux tooling in Rust to make software execution and system isolation seamless for Windows switchers.
- **Security & Privacy Lead / Director** at [**Bluelearn**](https://github.com/bluelearn-org/bluelearn) — Managing security and infrastructure for an open-source learning platform.

---

## MY ORGANIZATION : Ecosystem & Projects: [briDge](https://github.com/brRige)

> **Making Linux feel seamless for Windows switchers.**

Transitioning from Windows to Linux often comes with configuration friction. **briDge** builds straightforward CLI and GUI tools in Rust to remove these barriers.

### Core Launchers
| Project | Description | Status |
| :--- | :--- | :--- |
| **[wex](https://github.com/brRige/wex)** | A simplified Linux launcher for `.exe` applications built in Rust. | Active Development |
| **pex** | A high-performance executable launcher optimized specifically for Windows applications on Linux. | Planned / Up Next |

### Security & Tooling
| Project | Description | Status |
| :--- | :--- | :--- |
| **[patch-view](https://github.com/brRige/pvw)** | A lightweight CLI tool written in Rust to inspect binary headers, security flags, and executable dependencies before runtime. | Active Development |
| **wine-guard** | Sandbox and permission auditor to prevent Wine/Proton applications from accessing sensitive system directories. | Planned |
| **net-tracer** | Lightweight socket and network traffic inspector to monitor outbound executable connections. | Planned |

---

## Organizations I Am Working In 

### [Bluelearn](https://github.com/bluelearn-org/bluelearn)
> **Free knowledge, structured from the ground up.**  
> A non-profit, open-source education platform built around a prerequisite graph of concepts.

- **Role:** Director & Security / Privacy Lead
- **Security Focus:**
  - Performing security audits and dynamic vulnerability assessments across web APIs and microservices.
  - Designing rate-limiting algorithms, middleware sanitization layers, and Cloudflare WAF configurations.
  - Maintaining repository security policies, dependency audits, and authentication workflows.

---

## Repository Structure

```text
.
├── 📁 projects/              # Rust security utilities, binary inspection tools, & automation scripts
├── 📁 capture-the-flag/      # Writeups, notes, and solutions for CTF wargames (OverTheWire Bandit, etc.)
├── 📁 networking-and-labs/   # Packet analysis, network monitoring, and system configuration notes
└── 📁 certs-and-training/    # Documentation of formal security certifications and completed coursework
