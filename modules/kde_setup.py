from rich.console import Console
import subprocess
import os
from modules import utils

console = Console()

def install():
    console.print("[bold cyan]\n[+] Installing KDE Desktop and customizations...[/bold cyan]")

    try:
        kde_packages = ["kde-settings", "yakuake", "konsole", "ark", "plasma-nm"]
        if not utils.is_dnf_installed("plasma-workspace"):
            subprocess.run(["dnf", "groupinstall", "-y", "KDE Plasma Workspaces"], check=True)
        else:
            console.print("[green][✓] KDE Plasma already installed[/green]")

        for pkg in kde_packages:
            if not utils.is_dnf_installed(pkg):
                subprocess.run(["dnf", "install", "-y", pkg], check=True)
            else:
                console.print(f"[green][✓] {pkg} already installed[/green]")

        # Set KDE as default session
        xinit_path = os.path.expanduser("~/.xinitrc")
        if not os.path.exists(xinit_path) or "startplasma-x11" not in open(xinit_path).read():
            with open(xinit_path, "w") as f:
                f.write("exec startplasma-x11\n")
            console.print("[green][+] KDE session set in .xinitrc[/green]")

        # Set wallpaper if it exists
        wallpaper_path = "/opt/assets/background.png"
        if os.path.exists(wallpaper_path):
            dest_path = os.path.expanduser("~/Pictures/raccoon_bg.png")
            if not os.path.exists(dest_path):
                subprocess.run(["cp", wallpaper_path, dest_path], check=True)
            console.print("[green][✓] Wallpaper copied to Pictures[/green]")

        # Set custom Parrot-style prompt
        bashrc_path = os.path.expanduser("~/.bashrc")
        with open(bashrc_path, "r") as file:
            bashrc_contents = file.read()
        if "Parrot OS-style prompt" not in bashrc_contents:
            with open(bashrc_path, "a") as file:
                file.write("""\n# Parrot OS-style prompt
PS1=\"\\[\\033[0;31m\\]┌─\\[\\033[0;37m\\][\\[\\033[0;32m\\]\\u\\[\\033[0;37m\\]@\\[\\033[0;36m\\]\\h\\[\\033[0;37m\\]]\\[\\033[0;31m\\]─\\[\\033[0;37m\\][\\[\\033[0;33m\\]\\w\\[\\033[0;37m\\]]\\n\\[\\033[0;31m\\]└──╼ \\[\\033[0;33m\\]\\$\\[\\033[0m\\] \"\n""")
            console.print("[green][✓] Terminal prompt updated[/green]")
        else:
            console.print("[green][✓] Terminal prompt already configured[/green]")

        console.print("[bold green]\n✓ KDE and desktop customizations installed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Error installing KDE/prompt: {e}[/red]")
