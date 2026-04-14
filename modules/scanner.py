from core.utils import run_command

def quick_port_scan(target):
    cmd = f"nmap -Pn -T4 --top-ports 100 {target}"
    return run_command(cmd)

def service_scan(target):
    cmd = f"nmap -Pn -sV -T4 {target}"
    return run_command(cmd)
