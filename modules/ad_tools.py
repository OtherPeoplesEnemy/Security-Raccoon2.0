from rich.console import Console
import subprocess
import os
from modules import utils

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Active Directory tools...[/bold cyan]")

    try:
        dnf_packages = ["openldap-clients", "samba-client", "wmi-client", "powershell", "pipx", "unzip"]
        for pkg in dnf_packages:
            if not utils.is_dnf_installed(pkg):
                console.print(f"[yellow][-] Installing {pkg}...[/yellow]")
                subprocess.run(["dnf", "install", "-y", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} already installed[/green]")

        subprocess.run(["pipx", "ensurepath"], check=True)
        if not utils.is_pipx_installed("crackmapexec"):
            subprocess.run(["pipx", "install", "crackmapexec"], check=True)
        else:
            console.print("[green][✓] crackmapexec already installed via pipx[/green]")

        for pkg in ["ldapdomaindump"]:
            if not utils.is_pip_installed(pkg):
                subprocess.run(["pip3", "install", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} (pip) already installed[/green]")

        if not utils.is_command_available("kerbrute"):
            console.print("[yellow][-] Installing kerbrute...[/yellow]")
            os.environ["GOBIN"] = "/usr/local/bin"
            subprocess.run(["go", "install", "github.com/ropnop/kerbrute@latest"], check=True)
        else:
            console.print("[green][✓] kerbrute already installed[/green]")

        # enum4linux-ng
        if not utils.tool_exists("/opt/tools/enum4linux-ng"):
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/cddmp/enum4linux-ng.git", "/opt/tools/enum4linux-ng"], check=True)
        else:
            console.print("[green][✓] enum4linux-ng repo already exists[/green]")
        if not utils.is_command_available("enum4linux-ng"):
            subprocess.run(["ln", "-sf", "/opt/tools/enum4linux-ng/enum4linux-ng.py", "/usr/local/bin/enum4linux-ng"], check=True)

        # BloodHound GUI
        bh_gui_path = "/opt/bloodhound/BloodHound"
        if not utils.tool_exists(bh_gui_path):
            console.print("[yellow][-] Installing BloodHound GUI...[/yellow]")
            os.makedirs("/opt/bloodhound", exist_ok=True)
            subprocess.run([
                "wget",
                "https://github.com/SpecterOps/bloodhound/releases/latest/download/BloodHound-linux-x64.zip",
                "-O", "/tmp/BloodHound-linux-x64.zip"
            ], check=True)
            subprocess.run(["unzip", "-o", "/tmp/BloodHound-linux-x64.zip", "-d", "/opt/bloodhound"], check=True)
            subprocess.run(["ln", "-sf", bh_gui_path, "/usr/local/bin/bloodhound"], check=True)
        else:
            console.print("[green][✓] BloodHound GUI already installed[/green]")

        # BloodHound-python ingestor
        bh_py_path = "/opt/tools/bloodhound-python"
        if not utils.tool_exists(bh_py_path):
            console.print("[yellow][-] Installing bloodhound-python...[/yellow]")
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/SpecterOps/bloodhound-python.git", bh_py_path], check=True)
            subprocess.run(["pip3", "install", "-r", f"{bh_py_path}/requirements.txt"], check=True)
            subprocess.run(["ln", "-sf", f"{bh_py_path}/bloodhound-python.py", "/usr/local/bin/bloodhound-python"], check=True)
        else:
            console.print("[green][✓] bloodhound-python already cloned[/green]")

        console.print("[bold green]\n✓ Active Directory tools installed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing AD tools: {e}[/red]")
