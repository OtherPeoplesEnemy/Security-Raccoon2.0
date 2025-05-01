from rich.console import Console
import subprocess
from modules import utils

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
        for pkg in dnf_packages:
            if not utils.is_dnf_installed(pkg):
                console.print(f"[yellow][-] Installing {pkg}...[/yellow]")
                subprocess.run(["dnf", "install", "-y", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} already installed[/green]")

        subprocess.run(["pip3", "install", "--upgrade", "pip"], check=True)

        for pkg in pip_packages:
            if not utils.is_pip_installed(pkg):
                console.print(f"[yellow][-] Installing Python package: {pkg}...[/yellow]")
                subprocess.run(["pip3", "install", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} (pip) already installed[/green]")

        if not utils.is_command_available("evil-winrm"):
            subprocess.run(["gem", "install", "evil-winrm"], check=True)
        else:
            console.print("[green][✓] evil-winrm already installed[/green]")

        console.print("[bold green]\n✓ Core tools installed successfully![/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing core tools: {e}[/red]")
