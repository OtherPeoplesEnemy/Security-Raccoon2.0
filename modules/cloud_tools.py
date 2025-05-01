from rich.console import Console
import subprocess
import os
from modules import utils

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Cloud Pentest tools...[/bold cyan]")

    try:
        # CloudFox
        if not utils.tool_exists("/opt/tools/cloudfox"):
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/BishopFox/cloudfox.git", "/opt/tools/cloudfox"], check=True)
        else:
            console.print("[green][✓] CloudFox already cloned[/green]")

        # Sublist3r
        if not utils.tool_exists("/opt/tools/Sublist3r"):
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/aboul3la/Sublist3r.git", "/opt/tools/Sublist3r"], check=True)
        else:
            console.print("[green][✓] Sublist3r already cloned[/green]")

        subprocess.run(["pip3", "install", "-r", "/opt/tools/Sublist3r/requirements.txt"], check=False)

        # httpx
        if not utils.is_command_available("httpx"):
            console.print("[yellow][-] Installing httpx from Go...[/yellow]")
            subprocess.run(["go", "install", "github.com/projectdiscovery/httpx/cmd/httpx@latest"], check=True)
            subprocess.run(["cp", os.path.expanduser("~/go/bin/httpx"), "/usr/local/bin/httpx"], check=True)
        else:
            console.print("[green][✓] httpx already installed[/green]")

        console.print("[bold green]\n✓ Cloud tools installed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing cloud tools: {e}[/red]")
