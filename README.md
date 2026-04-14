# 🛡️ AI-Powered Cybersecurity CLI Assistant

<img width="937" height="964" alt="1" src="https://github.com/user-attachments/assets/02a216f3-c136-4435-956b-3f6c6c06fa53" />


> An advanced **AI-powered command-line cybersecurity assistant** for **Kali Linux**, built with **Python**, **Groq API**, and **Qwen3-32B**.  
> Designed for **SOC analysts**, **cybersecurity students**, **threat hunters**, and **blue team practitioners** to automate common security tasks directly from the terminal.

---

## 🚀 Project Overview

The **AI-Powered Cybersecurity CLI Assistant** is a terminal-based security companion that combines the power of:

- 🤖 **AI-driven analysis**
- 🔍 **Nmap scanning**
- 📜 **Log triage**
- 🧬 **YARA rule generation**
- 📈 **SIEM detection engineering**
- 🛡️ **Threat intelligence explanations**
- 📄 **Report generation**

This project is built specifically for **Kali Linux environments**, enabling security professionals to interact with a smart assistant directly from the command line for faster and more efficient defensive operations.

---

## 🎯 Key Features

### 🤖 AI Assistant Capabilities
- Natural language cybersecurity Q&A
- Threat intelligence explanations
- CVE analysis and summaries
- Defensive guidance and recommendations
- Incident response suggestions

### 🔎 Cybersecurity CLI Tools
- **Port Scanning** using Nmap
- **Service Enumeration** using Nmap
- **File Hashing** (MD5 + SHA256)
- **Security Log Analysis**
- **Threat Intel Lookup**
- **YARA Rule Generation**
- **SIEM Detection Query Generation**
- **Splunk SPL + Sigma Rule Suggestions**
- **Session Report Export**

---

## 🧠 Why This Project?

Security analysts often switch between multiple tools such as:

- Nmap
- log files
- SIEM platforms
- threat intelligence portals
- rule-writing workflows

This project **unifies those tasks into one AI-driven command-line interface**, making cybersecurity operations:

- ⚡ Faster
- 🧩 More efficient
- 🛠️ Easier to automate
- 🎓 Great for learning and lab environments

---

## 🏗️ Tech Stack

- **Python 3**
- **Groq API**
- **Qwen3-32B** (`qwen/qwen3-32b`)
- **Kali Linux**
- **Nmap**
- **Rich** (beautiful CLI UI)
- **python-dotenv**
- **pyfiglet**

---

## 📂 Project Structure

```bash
ai-cyber-cli/
│
├── .env
├── main.py
├── requirements.txt
│
├── core/
│   ├── config.py
│   ├── ui.py
│   ├── ai_client.py
│   ├── memory.py
│   └── utils.py
│
├── modules/
│   ├── scanner.py
│   ├── hash_tools.py
│   ├── log_analyzer.py
│   └── reporting.py
│
├── reports/
└── logs/
````

---

## ⚙️ Installation Guide (Kali Linux)

### 1️⃣ Update Kali Linux

```bash
sudo apt update && sudo apt upgrade -y
```

### 2️⃣ Install Required System Packages

```bash
sudo apt install -y python3 python3-pip python3-venv git curl nmap
```

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-cyber-cli.git
cd ai-cyber-cli
```

### 4️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=qwen/qwen3-32b
```

---

## 📦 requirements.txt

```txt
groq
python-dotenv
rich
pyfiglet
```

---

## ▶️ Running the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the assistant:

```bash
python3 main.py
```

---

## 💻 Available Commands

### General Commands

| Command | Description        |
| ------- | ------------------ |
| `help`  | Show help menu     |
| `clear` | Clear chat memory  |
| `exit`  | Exit the assistant |

### Cybersecurity Commands

| Command                  | Description                          |
| ------------------------ | ------------------------------------ |
| `ports <target>`         | Quick top 100 port scan              |
| `scan target <target>`   | Service/version scan with Nmap       |
| `hash file <path>`       | Generate MD5 + SHA256 hashes         |
| `analyze logs <path>`    | AI-powered log analysis              |
| `intel <CVE-ID>`         | Explain a CVE / threat               |
| `yara <description>`     | Generate YARA rule                   |
| `siem <attack/use-case>` | Generate SIEM/Splunk detection logic |
| `report`                 | Save current conversation report     |

---

## 🧪 Example Usage

### 🔎 Quick Port Scan

```bash
ports 127.0.0.1
```

### 🌐 Service Scan

```bash
scan target scanme.nmap.org
```

### 🔐 File Hashing

```bash
hash file /etc/hosts
```

### 📜 Log Analysis

```bash
analyze logs /var/log/auth.log
```

### 🧠 CVE Intelligence

```bash
intel CVE-2025-12345
```

### 🧬 Generate YARA Rule

```bash
yara ransomware behavior with file encryption and shadow copy deletion
```

### 📈 Generate SIEM Detection

```bash
siem ssh brute force on linux
```

### 📄 Save Session Report

```bash
report
```

---

## 🛡️ Security & Ethical Usage

> ⚠️ **Important Notice**

This project is intended for:

* Defensive cybersecurity
* Blue-team operations
* Security learning
* Lab / CTF / authorized environments
* Threat detection workflows

### ✅ Allowed / Intended Use

* Scan your own systems
* Analyze your own logs
* Create detection rules
* Learn security workflows
* Practice in legal lab environments

### ❌ Not Intended For

* Unauthorized scanning
* Offensive exploitation
* Malicious activity
* Destructive automation
* Illegal or unethical usage

---

## 🧱 Core Modules

### `core/config.py`

Stores:

* API key loading
* model name
* system prompt

### `core/ui.py`

Handles:

* CLI banner
* colored terminal output
* user input formatting

### `core/ai_client.py`

Responsible for:

* Groq API communication
* model calls
* conversation memory
* AI responses

### `core/memory.py`

Handles:

* saving chat history
* session persistence
* timestamps

### `core/utils.py`

Provides:

* safe subprocess execution
* utility helpers

### `modules/scanner.py`

Provides:

* quick port scanning
* service/version scanning

### `modules/hash_tools.py`

Provides:

* MD5 hashing
* SHA256 hashing

### `modules/log_analyzer.py`

Provides:

* secure log file reading
* truncated file ingestion for AI analysis

### `modules/reporting.py`

Provides:

* report generation
* report saving to `reports/`

---

## 🔥 Advanced Capabilities

This assistant can help with:

* SOC investigations
* Linux auth log analysis
* SSH brute force detection
* Sigma rule generation
* Splunk SPL generation
* Malware pattern explanation
* YARA rule writing
* Threat hunting ideas
* Incident response guidance
* Defensive playbook suggestions

---

## 📸 Sample Workflow

```bash
$ python3 main.py

You > help
You > ports 192.168.1.10
You > analyze logs /var/log/auth.log
You > intel CVE-2025-12345
You > yara ransomware behavior
You > siem suspicious ssh brute force
You > report
```

---

## 💡 Future Improvements

Planned enhancements for the professional version:

* [ ] Streaming AI responses
* [ ] Command auto-completion
* [ ] Better target validation
* [ ] Allowlisted safe command execution
* [ ] Threat intel API integrations
* [ ] VirusTotal hash lookups (optional API)
* [ ] MITRE ATT&CK mapping
* [ ] Suricata rule generation
* [ ] HTML/PDF report export
* [ ] Plugin-based architecture
* [ ] Interactive SOC workflow mode

---

## 🏆 Ideal Use Cases

This project is perfect for:

* 👨‍🎓 Cybersecurity students
* 🛡️ SOC analysts
* 🔍 Threat hunters
* 🧪 Blue-team labs
* 📚 Security learning environments
* 💼 Final-year academic projects
* 🧠 AI + Cybersecurity portfolio projects

---

## 📚 Educational Value

This project demonstrates practical knowledge in:

* Python automation
* Secure CLI application design
* API integration
* Prompt engineering
* Defensive cybersecurity
* Nmap automation
* Log analysis
* Detection engineering
* Threat intelligence workflows
* Blue-team tooling

---

## 🎓 Academic / Portfolio Project Title

**AI-Powered Cybersecurity CLI Assistant for Kali Linux using Groq API and Qwen3-32B**

### Suggested Problem Statement

Security analysts often rely on multiple disconnected tools for scanning, log analysis, threat intelligence, and detection engineering. This project integrates these workflows into a unified AI-driven command-line assistant to improve speed, usability, and learning efficiency in cybersecurity operations.

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 🐞 Common Issues

### `GROQ_API_KEY not found`

Make sure your `.env` file exists and contains:

```env
GROQ_API_KEY=your_key_here
```

### `ModuleNotFoundError`

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

### `nmap: command not found`

Install Nmap:

```bash
sudo apt install -y nmap
```

---

## 📜 License

This project is licensed under the **MIT License**.
You may use, modify, and distribute it for educational and professional purposes.

---

## ⭐ Support This Project

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Share it with cybersecurity learners
* 🚀 Use it in your portfolio / final-year project

---

## 👨‍💻 Author

**Gaurav Ghandat**
Cybersecurity & AI Enthusiast
Built with ❤️ on **Kali Linux**

---

## 🔥 Final Note

This project combines the power of:

* **Artificial Intelligence**
* **Cybersecurity Automation**
* **Kali Linux Tooling**
* **Blue Team Workflows**

It’s not just a CLI bot — it’s a **smart cybersecurity companion for the terminal**.

> **Think like an analyst. Automate like an engineer. Defend like a pro.**

---

