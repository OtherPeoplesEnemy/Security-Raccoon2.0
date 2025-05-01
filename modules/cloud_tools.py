from rich.console import Console
import subprocess
import os

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Cloud Pentest tools...[/bold cyan]")

    try:
        # Clone CloudFox
        subprocess.run(["git", "clone", "https://github.com/BishopFox/cloudfox.git", "/opt/tools/cloudfox"], check=False)

        # Install Sublist3r
        subprocess.run(["git", "clone", "https://github.com/aboul3la/Sublist3r.git", "/opt/tools/Sublist3r"], check=False)
        subprocess.run(["pip3", "install", "-r", "/opt/tools/Sublist3r/requirements.txt"], check=False)

        # Install httpx
        subprocess.run(["go", "install", "github.com/projectdiscovery/httpx/v2/cmd/httpx@latest"], check=True)
        subprocess.run(["cp", os.path.expanduser("~/go/bin/httpx"), "/usr/local/bin/httpx"], check=False)

        console.print("[green]✓ Cloud tools installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing cloud tools: {e}[/red]")
