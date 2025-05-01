from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from modules import core_tools, ad_tools, cloud_tools, c2s, kde_setup

console = Console()

def main_menu():
    while True:
        console.print(Panel.fit("[bold cyan]Security Raccoon Installer[/bold cyan] 🦝"))
        console.print("Select a category to install:\n")
        console.print("[1] Core Pentest Tools")
        console.print("[2] Active Directory Tools")
        console.print("[3] Cloud Tools")
        console.print("[4] C2 Frameworks (Empire, Sliver)")
        console.print("[5] Desktop Environment & Customization")
        console.print("[6] Install Everything")
        console.print("[0] Exit\n")

        choice = Prompt.ask("[bold green]Enter your choice[/bold green]", choices=["1", "2", "3", "4", "5", "6", "0"], default="0")

        if choice == "1":
            core_tools.install()
        elif choice == "2":
            ad_tools.install()
        elif choice == "3":
            cloud_tools.install()
        elif choice == "4":
            c2s.install()
        elif choice == "5":
            kde_setup.install()
        elif choice == "6":
            console.print("[yellow]\nInstalling EVERYTHING... grab some coffee ☕\n[/yellow]")
            core_tools.install()
            ad_tools.install()
            cloud_tools.install()
            c2s.install()
            kde_setup.install()
            console.print("[bold green]\n✓ All tools installed successfully![/bold green]")
        elif choice == "0":
            console.print("[bold red]Exiting installer. Goodbye![/bold red]")
            break

        input("\n[Press Enter to return to the main menu]")

if __name__ == "__main__":
    main_menu()
