from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

def show_banner():
    banner = pyfiglet.figlet_format("AI CYBER CLI", font="slant")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print(Panel.fit(
        "[bold green]AI-Powered Cybersecurity CLI Assistant[/bold green]\n"
        "[yellow]Groq API + Qwen3 32B + Kali Linux[/yellow]",
        border_style="cyan"
    ))

def print_info(msg):
    console.print(f"[bold blue][*][/bold blue] {msg}")

def print_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def print_error(msg):
    console.print(f"[bold red][-][/bold red] {msg}")

def print_bot(msg):
    console.print(Panel(msg, title="🤖 Assistant", border_style="cyan"))

def get_user_input():
    return console.input("[bold green]You > [/bold green]")
