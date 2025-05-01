from rich.console import Console
import subprocess

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing core pentest tools...[/bold cyan]")

    dnf_packages = [
        "nmap", "wireshark", "aircrack-ng", "john", "gobuster", "nikto",
        "ffuf", "git", "python3-pip", "cmake", "gcc", "g++", "make",
        "unzip", "wget", "curl", "ruby"
    ]

    pip_packages = ["impacket", "sqlmap"]

    try:
        subprocess.run(["dnf", "install", "-y"] + dnf_packages, check=True)
        subprocess.run(["pip3", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["pip3", "install"] + pip_packages, check=True)
        subprocess.run(["gem", "install", "evil-winrm"], check=True)
        console.print("[green]✓ Core tools installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing core tools: {e}[/red]")
