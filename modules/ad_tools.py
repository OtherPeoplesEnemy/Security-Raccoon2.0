from rich.console import Console
import subprocess
import os

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Active Directory tools...[/bold cyan]")

    try:
        # Install DNF packages
        dnf_packages = [
            "openldap-clients", "samba-client", "wmi-client", "powershell", "pipx"
        ]
        subprocess.run(["dnf", "install", "-y"] + dnf_packages, check=True)

        # Ensure pipx is set up
        subprocess.run(["pipx", "ensurepath"], check=True)
        subprocess.run(["pipx", "install", "crackmapexec"], check=True)

        # Python AD tools
        subprocess.run(["pip3", "install", "ldapdomaindump", "bloodhound"], check=True)

        # Go tool: kerbrute
        subprocess.run(["dnf", "install", "-y", "golang"], check=True)
        os.environ["GOBIN"] = "/usr/local/bin"
        subprocess.run(["go", "install", "github.com/ropnop/kerbrute@latest"], check=True)

        # Clone enum4linux-ng
        subprocess.run(["git", "clone", "https://github.com/cddmp/enum4linux-ng.git", "/opt/tools/enum4linux-ng"], check=False)
        subprocess.run(["ln", "-sf", "/opt/tools/enum4linux-ng/enum4linux-ng.py", "/usr/local/bin/enum4linux-ng"], check=False)

        console.print("[green]✓ Active Directory tools installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing AD tools: {e}[/red]")
