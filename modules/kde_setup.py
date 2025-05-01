from rich.console import Console
import subprocess
import os

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing KDE Desktop and customizations...[/bold cyan]")

    try:
        # Install KDE
        subprocess.run(["dnf", "groupinstall", "-y", "KDE Plasma Workspaces"], check=True)
        subprocess.run(["dnf", "install", "-y", "kde-settings", "yakuake", "konsole", "ark", "plasma-nm"], check=True)

        # Set KDE session
        subprocess.run(["bash", "-c", "echo 'exec startplasma-x11' > ~/.xinitrc"], check=True)

        # Set custom wallpaper if present
        wallpaper_path = "/opt/assets/background.png"
        if os.path.exists(wallpaper_path):
            os.makedirs(os.path.expanduser("~/Pictures"), exist_ok=True)
            subprocess.run(["cp", wallpaper_path, os.path.expanduser("~/Pictures/raccoon_bg.png")], check=True)

        # Parrot-style terminal prompt
        prompt = """\n# Parrot OS-style prompt
PS1=\"\\[\\033[0;31m\\]┌─\\[\\033[0;37m\\][\\[\\033[0;32m\\]\\u\\[\\033[0;37m\\]@\\[\\033[0;36m\\]\\h\\[\\033[0;37m\\]]\\[\\033[0;31m\\]─\\[\\033[0;37m\\][\\[\\033[0;33m\\]\\w\\[\\033[0;37m\\]]\\n\\[\\033[0;31m\\]└──╼ \\[\\033[0;33m\\]\\$\\[\\033[0m\\] \"\n"""
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(prompt)

        console.print("[green]✓ KDE and desktop customizations installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing KDE/prompt: {e}[/red]")
