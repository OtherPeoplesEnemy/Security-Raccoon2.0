from rich.console import Console
import subprocess
import os

def tool_exists(path):
    return os.path.exists(path)

def is_command_available(cmd):
    return subprocess.run(["which", cmd], stdout=subprocess.DEVNULL).returncode == 0

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing Command & Control tools...[/bold cyan]")

    try:
        os.makedirs("/opt/tools", exist_ok=True)

        # Sliver C2
        sliver_path = "/opt/tools/sliver-server"
        if not tool_exists(sliver_path):
            subprocess.run([
                "wget",
                "https://github.com/BishopFox/sliver/releases/latest/download/sliver-server_linux",
                "-O", sliver_path
            ], check=True)
            subprocess.run(["chmod", "+x", sliver_path], check=True)
        else:
            console.print("[green][✓] Sliver C2 binary already exists[/green]")

        if not is_command_available("sliver-server"):
            subprocess.run(["ln", "-sf", sliver_path, "/usr/local/bin/sliver-server"], check=True)

        # Empire
        empire_dir = "/opt/tools/Empire"
        if not tool_exists(empire_dir):
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/BC-SECURITY/Empire.git", empire_dir], check=True)
            subprocess.run(["bash", f"{empire_dir}/setup/install.sh"], check=True)
        else:
            console.print("[green][✓] Empire already cloned[/green]")

        console.print("[bold green]\n✓ C2 tools installed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing C2 tools: {e}[/red]")
