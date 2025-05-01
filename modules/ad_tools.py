from rich.console import Console
import subprocess
import os
from modules import utils

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Active Directory tools...[/bold cyan]")

    try:
        dnf_packages = ["openldap-clients", "samba-client", "wmi-client", "powershell", "pipx"]

        for pkg in dnf_packages:
            if not utils.is_dnf_installed(pkg):
                console.print(f"[yellow][-] Installing {pkg}...[/yellow]")
                subprocess.run(["dnf", "install", "-y", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} already installed[/green]")

        # pipx ensurepath and CrackMapExec
        subprocess.run(["pipx", "ensurepath"], check=True)
        if not utils.is_pipx_installed("crackmapexec"):
            subprocess.run(["pipx", "install", "crackmapexec"], check=True)
        else:
            console.print("[green][✓] crackmapexec already installed via pipx[/green]")

        # Python tools
        for pkg in ["ldapdomaindump", "bloodhound"]:
            if not utils.is_pip_installed(pkg):
                console.print(f"[yellow][-] Installing {pkg}...[/yellow]")
                subprocess.run(["pip3", "install", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} (pip) already installed[/green]")

        # Go tool: kerbrute
        if not utils.is_command_available("kerbrute"):
            console.print("[yellow][-] Installing kerbrute...[/yellow]")
            os.environ["GOBIN"] = "/usr/local/bin"
            subprocess.run(["go", "install", "github.com/ropnop/kerbrute@latest"], check=True)
        else:
            console.print("[green][✓] kerbrute already installed[/green]")

        # enum4linux-ng
        if not utils.tool_exists("/opt/tools/enum4linux-ng"):
            subprocess.run(["git", "clone", "https://github.com/cddmp/enum4linux-ng.git", "/opt/tools/enum4linux-ng"], check=True)
        else:
            console.print("[green][✓] enum4linux-ng repo already exists[/green]")

        if not utils.is_command_available("enum4linux-ng"):
            subprocess.run(["ln", "-sf", "/opt/tools/enum4linux-ng/enum4linux-ng.py", "/usr/local/bin/enum4linux-ng"], check=True)

        console.print("[bold green]\n✓ Active Directory tools installed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing AD tools: {e}[/red]")
