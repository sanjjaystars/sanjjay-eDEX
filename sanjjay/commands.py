"""Command handlers for the sanjjay CLI."""

from __future__ import annotations

import random
import time

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .data import COMMAND_DESCRIPTIONS, PROFILE, PROJECTS
from .ui import fake_system_metrics, render_banner, render_header

console = Console()


class CommandHandler:
    """Resolve and execute user commands."""

    def __init__(self, start_time: float) -> None:
        self.start_time = start_time

    def execute(self, command: str) -> bool:
        handlers = {
            "help": self.help,
            "about": self.about,
            "skills": self.skills,
            "projects": self.projects,
            "github": self.github,
            "linkedin": self.linkedin,
            "contact": self.contact,
            "resume": self.resume,
            "clear": self.clear,
            "whoami": self.whoami,
            "socials": self.socials,
            "banner": self.banner,
            "system": self.system,
            "exit": self.exit,
            "quit": self.exit,
        }

        if not command:
            return True

        handler = handlers.get(command.lower())
        if handler is None:
            console.print(f"[red]Unknown command:[/red] [white]{command}[/white]. Try [bold]help[/bold].")
            return True

        return handler()

    def help(self) -> bool:
        table = Table(title="Command Reference", border_style="grey50")
        table.add_column("Command", style="white", no_wrap=True)
        table.add_column("Description", style="grey78")

        for cmd, description in COMMAND_DESCRIPTIONS.items():
            table.add_row(cmd, description)

        console.print(table)
        return True

    def about(self) -> bool:
        profile = PROFILE
        body = f"[bold white]{profile['name']}[/bold white]\n[grey70]{profile['role']}[/grey70]\n\n{profile['bio']}"
        console.print(Panel(body, border_style="grey50", title="about"))
        return True

    def skills(self) -> bool:
        table = Table(title="Skills Matrix", border_style="grey50")
        table.add_column("Domain", style="white", no_wrap=True)
        table.add_column("Stack", style="grey78")
        for category, items in PROFILE["skills"].items():
            table.add_row(category, " • ".join(items))
        console.print(table)
        return True

    def projects(self) -> bool:
        table = Table(title="Featured Projects", border_style="grey50")
        table.add_column("Project", style="white", no_wrap=True)
        table.add_column("Description", style="grey78")
        table.add_column("Tech Stack", style="grey70")
        table.add_column("Links", style="bright_white")

        for project in PROJECTS:
            links = f"[link={project.github}]GitHub[/link] | [link={project.demo}]Demo[/link]"
            table.add_row(project.name, project.description, project.stack, links)

        console.print(table)
        return True

    def github(self) -> bool:
        console.print(f"[bold white]GitHub:[/bold white] {PROFILE['socials']['github']}")
        return True

    def linkedin(self) -> bool:
        console.print(f"[bold white]LinkedIn:[/bold white] {PROFILE['socials']['linkedin']}")
        return True

    def contact(self) -> bool:
        contact = PROFILE["contact"]
        table = Table(title="Contact", border_style="grey50")
        table.add_column("Field", style="white")
        table.add_column("Value", style="grey78")
        table.add_row("Phone", contact["phone"])
        table.add_row("Email", contact["email"])
        table.add_row("Location", contact["location"])
        console.print(table)
        return True

    def resume(self) -> bool:
        console.print(f"[bold white]Resume:[/bold white] {PROFILE['socials']['resume']}")
        return True

    def clear(self) -> bool:
        console.clear()
        render_banner()
        render_header()
        return True

    def whoami(self) -> bool:
        aliases = ["root_operator", "packet_hunter", "shadow_builder", "cipher_dev"]
        label = random.choice(aliases)
        lines = [
            f"identity : {PROFILE['name']} ({label})",
            f"mission  : Build secure systems with premium UX",
            "status   : ACTIVE // DEFENSIVE MODE",
        ]
        console.print(Panel("\n".join(lines), title="whoami", border_style="grey50"))
        return True

    def socials(self) -> bool:
        table = Table(title="Social Endpoints", border_style="grey50")
        table.add_column("Platform", style="white")
        table.add_column("URL", style="grey78")
        for platform, link in PROFILE["socials"].items():
            table.add_row(platform.title(), link)
        console.print(table)
        return True

    def banner(self) -> bool:
        render_banner()
        return True

    def system(self) -> bool:
        console.print(Panel(fake_system_metrics(self.start_time), border_style="grey50", title="system telemetry"))
        return True

    def exit(self) -> bool:
        with console.status("[grey70]Closing secure session...", spinner="dots"):
            time.sleep(0.6)
        console.print("[bold white]Session terminated.[/bold white] [grey58]Stay sharp.[/grey58]")
        return False
