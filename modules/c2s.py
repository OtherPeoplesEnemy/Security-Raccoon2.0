from rich.console import Console
import subprocess
import os

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Command & Control tools...[/bold cyan]")

    try:
        os.makedirs("/opt/tools", exist_ok=True)

        # Install Sliver
        subprocess.run([
            "wget",
            "https://github.com/BishopFox/sliver/releases/latest/download/sliver-server_linux",
            "-O", "/opt/tools/sliver-server"
        ], check=True)
        subprocess.run(["chmod", "+x", "/opt/tools/sliver-server"], check=True)
        subprocess.run(["ln", "-sf", "/opt/tools/sliver-server", "/usr/local/bin/sliver-server"], check=False)

        # Install Empire
        subprocess.run(["git", "clone", "https://github.com/BC-SECURITY/Empire.git", "/opt/tools/Empire"], check=False)
        subprocess.run(["/opt/tools/Empire/setup/install.sh", "--yes"], check=False)

        console.print("[green]✓ C2 tools installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing C2 tools: {e}[/red]")
