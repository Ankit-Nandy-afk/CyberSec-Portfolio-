# 🗺️ OverTheWire: Bandit Wargame Chronicles

> A comprehensive log of my journey mastering Linux fundamentals, security concepts, and shell wizardry through the classic OverTheWire Bandit challenges.

---

## 📊 Campaign Progress

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

| Objective | Progress Bar | Current Status |
| :--- | :--- | :--- |
| **Bandit Levels 0 → 34** | `████░░░░░░░░░░░░░░░░░░░░░░░░░░` | 🚀 Active Operation |

---

## 🥷 Mission Log & Technical Writeups

### 🟢 Foundation Levels (0 → 10)

<details>
<summary><b>Level 0 → Level 1: The Absolute Basics</b></summary>

* **Core Concepts:** Directory Listing, File Inspection
* **Commands Used:** `ls`, `cat`
* **Writeup:** Used `ls` to find the target file in the home directory and printed its text contents to clear the level using `cat`.
</details>

<details>
<summary><b>Level 1 → Level 2: The Dash File</b></summary>

* **Core Concepts:** Dash-prefixed filenames, Shell arguments
* **Commands Used:** `cat ./-`
* **Writeup:** A filename named `-` confuses standard flags. Used relative pathing `./-` to reference it safely.
</details>

<details>
<summary><b>Level 2 → Level 3: Spaces in Filenames</b></summary>

* **Core Concepts:** Handling whitespaces via escaping/quoting
* **Commands Used:** `cat "spaces in this filename"`
* **Writeup:** Wrapped the multi-word file name in quotes to prevent the terminal from treating it as separate arguments.
</details>

<details>
<summary><b>Level 3 → Level 4: Hidden Treasures</b></summary>

* **Core Concepts:** Hidden files (dotfiles)
* **Commands Used:** `ls -la`, `cat`
* **Writeup:** Standard `ls` hides dotfiles. Used `-la` to uncover the hidden directory contents.
</details>

<details>
<summary><b>Level 4 → Level 5: Human Readable Data</b></summary>

* **Core Concepts:** Data types, file inspection
* **Commands Used:** `file`, `cat`
* **Writeup:** Used a wildcard loop or `file ./*` to distinguish ASCII text from raw binary objects.
</details>

<details>
<summary><b>Level 5 → Level 6: Finding a Needle</b></summary>

* **Core Concepts:** Recursive searching with size constraints
* **Commands Used:** `find . -type f -size 1033c ! -executable`
* **Writeup:** Leveraged specific target criteria filters like byte size (`c`) and execution properties to find the specific file.
</details>

<details>
<summary><b>Level 6 → Level 7: System-Wide Hunts</b></summary>

* **Core Concepts:** User/Group permissions, filtering standard error (`2>/dev/null`)
* **Commands Used:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`
* **Writeup:** Searched root paths while cleanly piping permission-denied warnings to the null device.
</details>

<details>
<summary><b>Level 7 → Level 8: Grabbing Patterns</b></summary>

* **Core Concepts:** Piping stream text, pattern matching
* **Commands Used:** `grep "millionth" data.txt`
* **Writeup:** Filtered a large textual dump to instantly pull out the password next to the keyword.
</details>

<details>
<summary><b>Level 8 → Level 9: Unique Occurrences</b></summary>

* **Core Concepts:** Stream manipulation, sorting
* **Commands Used:** `sort data.txt | uniq -u`
* **Writeup:** `uniq` strictly requires sorted streams. Combined both to spot the single non-repeating line.
</details>

<details>
<summary><b>Level 9 → Level 10: Human Strings inside Binary</b></summary>

* **Core Concepts:** Extracting readable content from binary dumps
* **Commands Used:** `strings data.txt | grep "=="`
* **Writeup:** Stripped out unreadable junk artifacts to view plain characters preceding equal signs.
</details>

---

### 🟡 Intermediate Core (10 → 20)

<details>
<summary><b>Level 10 → Level 11: Base64 Decoding</b></summary>

* **Core Concepts:** Data encoding transformations
* **Commands Used:** `base64 -d data.txt`
* **Writeup:** Decoded the string back into human-readable text.
</details>

<details>
<summary><b>Level 11 → Level 12: ROT13 Cypher</b></summary>

* **Core Concepts:** Caesar substitution cyphers
* **Commands Used:** `tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt`
* **Writeup:** Handled character rotation to shift the ciphered string 13 steps down.
</details>

<details>
<summary><b>Level 12 → Level 13: Hex Dumps and Decompression</b></summary>

* **Core Concepts:** Reversing hex dumps, layered compression architectures
* **Commands Used:** `xxd -r`, `gzip`, `bzip2`, `tar`
* **Writeup:** Repeatedly unpacked nested compressions step-by-step by checking file headers until getting the raw text.
</details>

<details>
<summary><b>Level 13 → Level 14: SSH Keys</b></summary>

* **Core Concepts:** Asymmetric keys, private identity flags
* **Commands Used:** `ssh -i sshkey.private bandit14@localhost -p 2220`
* **Writeup:** Logged in directly using an identity file block instead of a standard string password.
</details>

<details>
<summary><b>Level 14 → Level 15: Local Network Pipes</b></summary>

* **Core Concepts:** Port interaction, sockets
* **Commands Used:** `nc localhost 30000`
* **Writeup:** Transmitted the previous stage's string through Netcat to the specific listening port.
</details>

<details>
<summary><b>Level 15 → Level 16: SSL/TLS Connections</b></summary>

* **Core Concepts:** Secure encrypted sockets
* **Commands Used:** `openssl s_client -connect localhost:30001`
* **Writeup:** Exchanged passwords over a secure handshake stream instead of a raw socket connection.
</details>

<details>
<summary><b>Level 16 → Level 17: Port Scanning</b></summary>

* **Core Concepts:** Network discovery
* **Commands Used:** `nmap -p 31000-32000 localhost`
* **Writeup:** Scanned a specified range to uncover listening SSL sockets, then parsed for valid credentials.
</details>

<details>
<summary><b>Level 17 → Level 18: File Diffs</b></summary>

* **Core Concepts:** File comparisons
* **Commands Used:** `diff passwords.old passwords.new`
* **Writeup:** Compared file versions side-by-side to target the single line variation.
</details>

<details>
<summary><b>Level 18 → Level 19: SSH Shell Bypassing</b></summary>

* **Core Concepts:** Forced command profile execution overrides
* **Commands Used:** `ssh bandit18@localhost -p 2220 "cat readme"`
* **Writeup:** Prevented the immediate logout routine by executing the targeted string payload along with the login command directly.
</details>

<details>
<summary><b>Level 19 → Level 20: SetUID Binaries</b></summary>

* **Core Concepts:** SetUID logic, privilege escalation
* **Commands Used:** `./bandit20-do cat /etc/bandit_pass/bandit20`
* **Writeup:** Leveraged a binary designed to briefly scale permissions to inspect forbidden access files.
</details>

---

### 🟠 Advanced Scripting & Processes (20 → 30)

<details>
<summary><b>Level 20 → Level 21: Port Listeners</b></summary>

* **Core Concepts:** Backgrounding processes, simultaneous port listening
* **Commands Used:** `nc -lvp 4444 &`, `./suconnect 4444`
* **Writeup:** Created a local network hook, backgrounded it, and pointed the checking executable straight to it.
</details>

<details>
<summary><b>Level 21 → Level 22: Cron Jobs</b></summary>

* **Core Concepts:** Automation daemons
* **Commands Used:** `cat /etc/cron.d/`, `cat /usr/bin/cronjob_bandit22.sh`
* **Writeup:** Read scheduled background operations to pinpoint target logging destinations.
</details>

<details>
<summary><b>Level 22 → Level 23: Deconstructing Cron Scripts</b></summary>

* **Core Concepts:** Reverse engineering shell logic
* **Commands Used:** Modulo hashing analysis inside shell logic scripts
* **Writeup:** Followed MD5 hashing string routines inside an automated script to find where the password was saved.
</details>

<details>
<summary><b>Level 23 → Level 24: Writing Cron Payloads</b></summary>

* **Core Concepts:** Custom script execution via cron directories
* **Commands Used:** `chmod 777`, writing custom `.sh` transfer operations
* **Writeup:** Put a custom script into an automated target directory that copied root password structures out to `/tmp`.
</details>

<details>
<summary><b>Level 24 → Level 25: Bruteforcing Pins</b></summary>

* **Core Concepts:** Network scripting loops
* **Commands Used:** Bash `for` loop, nested variables, `nc`
* **Writeup:** Wrote a compact loop sequence to blast all 10,000 combinations into a stubborn port check tool.
</details>

<details>
<summary><b>Level 25 → Level 26: Custom Shell Breakouts</b></summary>

* **Core Concepts:** Overriding default shell locks
* **Commands Used:** Text window resizing tricks, `v` text editor command expansions
* **Writeup:** Shrank the terminal window to trap the session in a text viewer (`more`), then broke out using its built-in editor triggers.
</details>

<details>
<summary><b>Level 26 → Level 27: Shell Scaling Escalation</b></summary>

* **Core Concepts:** Executing system shells inside editors
* **Commands Used:** `:set shell=/bin/bash`, `:sh`
* **Writeup:** Redefined variable paths within the text editor framework to gain a functional bash environment.
</details>

<details>
<summary><b>Level 27 → Level 28: Git Cloning Basics</b></summary>

* **Core Concepts:** Interacting with local version control
* **Commands Used:** `git clone ssh://...`
* **Writeup:** Cloned an internal repository down into a temporary workspace to extract data.
</details>

<details>
<summary><b>Level 28 → Level 29: Git Log Inspections</b></summary>

* **Core Concepts:** Commit history auditing
* **Commands Used:** `git log -p`, `git show`
* **Writeup:** Unearthed values that were previously written and later deleted by inspecting old commit states.
</details>

<details>
<summary><b>Level 29 → Level 30: Checking Git Branches</b></summary>

* **Core Concepts:** Isolated version control tracking
* **Commands Used:** `git branch -a`, `git checkout`
* **Writeup:** Audited hidden development streams within a codebase to find tucked-away credential secrets.
</details>

---

### 🔴 Expert Levels (30 → 34)

<details>
<summary><b>Level 30 → Level 31: Auditing Git Tags</b></summary>

* **Core Concepts:** Version tags, release tracking
* **Commands Used:** `git tag`, `git show`
* **Writeup:** Audited static tags pinned onto specific milestone branches to retrieve metadata logs.
</details>

<details>
<summary><b>Level 31 → Level 32: Pushing to Remote Repositories</b></summary>

* **Core Concepts:** Local git staging files, push tracking
* **Commands Used:** `git add -f`, `git commit`, `git push`
* **Writeup:** Forced an tracking ignore override (`.gitignore`) to commit and push a file up to master.
</details>

<details>
<summary><b>Level 32 → Level 33: Escape from UpperCase Shells</b></summary>

* **Core Concepts:** Shell variable evaluation escapes
* **Commands Used:** `$0` positional extraction execution
* **Writeup:** Passed standard environmental variables directly into execution arguments to spawn a true bash session out of a restricted shell context.
</details>

<details>
<summary><b>Level 33 → Level 34: The Final Frontier</b></summary>

* **Core Concepts:** Culmination of the journey
* **Commands Used:** Global system inspection
* **Writeup:** Successfully cleared the challenge series, unlocking the ultimate confirmation key.
</details>

---