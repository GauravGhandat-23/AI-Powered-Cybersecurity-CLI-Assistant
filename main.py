from core.ui import show_banner, print_info, print_success, print_error, print_bot, get_user_input
from core.ai_client import AIClient
from core.memory import save_history
from modules.scanner import quick_port_scan, service_scan
from modules.hash_tools import file_hashes
from modules.log_analyzer import read_log_file
from modules.reporting import save_report

HELP_TEXT = """
Available Commands:
  help                              Show help menu
  clear                             Clear chat memory
  exit                              Exit the assistant

Cybersecurity Commands:
  ports <target>                    Quick top 100 port scan
  scan target <target>              Service/version scan with Nmap
  hash file <path>                  Generate MD5 + SHA256
  analyze logs <path>               AI analyze a log file
  intel <CVE-ID>                    Explain a CVE / threat
  yara <description>                Generate YARA rule
  siem <attack/use-case>            Generate SIEM/Splunk detection logic
  report                            Save current conversation report

Examples:
  ports 127.0.0.1
  scan target scanme.nmap.org
  hash file /home/kali/sample.exe
  analyze logs /var/log/auth.log
  intel CVE-2025-12345
  yara ransomware behavior with file encryption and shadow copy deletion
  siem brute force login attempts on Linux SSH
"""

def main():
    show_banner()
    print_info("Type 'help' to see available commands.")

    ai = AIClient()

    while True:
        try:
            user_input = get_user_input().strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                save_history(ai.get_history())
                print_success("Session saved. Goodbye!")
                break

            elif user_input.lower() == "help":
                print_bot(HELP_TEXT)

            elif user_input.lower() == "clear":
                ai.clear_memory()
                print_success("Conversation memory cleared.")

            elif user_input.lower().startswith("ports "):
                target = user_input[6:].strip()
                print_info(f"Running quick port scan on {target} ...")
                result = quick_port_scan(target)
                print_bot(result)

            elif user_input.lower().startswith("scan target "):
                target = user_input[12:].strip()
                print_info(f"Running service scan on {target} ...")
                result = service_scan(target)
                print_bot(result)

            elif user_input.lower().startswith("hash file "):
                path = user_input[10:].strip()
                hashes = file_hashes(path)
                if "error" in hashes:
                    print_error(hashes["error"])
                else:
                    result = f"MD5: {hashes['md5']}\nSHA256: {hashes['sha256']}"
                    print_bot(result)

            elif user_input.lower().startswith("analyze logs "):
                path = user_input[13:].strip()
                content, err = read_log_file(path)
                if err:
                    print_error(err)
                else:
                    prompt = f"""
Analyze the following security log content from a Kali Linux environment.

Tasks:
1. Identify suspicious patterns
2. Highlight brute force / failed logins / privilege escalation indicators
3. Summarize key findings
4. Suggest next investigation steps
5. Recommend defensive actions

Log Content:
{content}
"""
                    reply = ai.ask(prompt)
                    print_bot(reply)

            elif user_input.lower().startswith("intel "):
                cve = user_input[6:].strip()
                prompt = f"""
Provide a defensive cybersecurity intelligence summary for: {cve}

Include:
- What it is
- Potential impact
- Common attack path
- Detection ideas
- Mitigation steps
- Safe lab learning note
"""
                reply = ai.ask(prompt)
                print_bot(reply)

            elif user_input.lower().startswith("yara "):
                desc = user_input[5:].strip()
                prompt = f"""
Generate a YARA rule for this malware/threat description:
{desc}

Requirements:
- valid YARA syntax
- include comments
- explain what each section does
- keep it defensive and educational
"""
                reply = ai.ask(prompt)
                print_bot(reply)

            elif user_input.lower().startswith("siem "):
                use_case = user_input[5:].strip()
                prompt = f"""
Create a SIEM detection for this use case:
{use_case}

Include:
1. Detection logic
2. Splunk SPL example
3. Sigma rule example
4. False positives
5. Tuning advice
"""
                reply = ai.ask(prompt)
                print_bot(reply)

            elif user_input.lower() == "report":
                history = ai.get_history()
                text = "\n\n".join([f"{m['role'].upper()}:\n{m['content']}" for m in history])
                filename = save_report(text)
                print_success(f"Report saved: {filename}")

            else:
                reply = ai.ask(user_input)
                print_bot(reply)

        except KeyboardInterrupt:
            print_error("Interrupted. Type 'exit' to quit safely.")
        except Exception as e:
            print_error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
