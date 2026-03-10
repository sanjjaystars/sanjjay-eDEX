"""Rendering helpers for the terminal dashboard."""

from __future__ import annotations

import random
import time
from datetime import datetime

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

from .data import PROFILE

console = Console()

ASCII_BANNER = r"""
  _____          _   _       _       __     __
 / ____|   /\   | \ | |     | |      \ \   / /
| (___    /  \  |  \| |     | |       \ \_/ / 
 \___ \  / /\ \ | . ` | _   | |        \   /  
 ____) |/ ____ \| |\  || |__| |         | |   
|_____//_/    \_\_| \_| \____/          |_|   
"""


def clear_screen() -> None:
    console.clear()


def render_banner() -> None:
    banner = Text(ASCII_BANNER, style="bold bright_white")
    subtitle = Text("eDEX-style terminal portfolio", style="grey70")
    panel = Panel(
        Align.center(Text.assemble(banner, "\n", subtitle)),
        border_style="grey50",
        title="[bold white]SANJJAY CORE[/bold white]",
        subtitle="[grey62]secure • minimal • futuristic[/grey62]",
    )
    console.print(panel)


def render_header() -> None:
    profile = PROFILE
    identity = Table.grid(padding=(0, 2))
    identity.add_column(style="grey70")
    identity.add_column(style="bright_white")
    identity.add_row("operator", profile["name"])
    identity.add_row("role", profile["role"])
    identity.add_row("host", profile["hostname"])
    identity.add_row("os", profile["os"])
    identity.add_row("terminal", profile["terminal"])

    console.print(Panel(identity, border_style="grey50", title="[white]session identity[/white]"))
    console.print(Rule("[grey58]interactive command console[/grey58]", style="grey39"))


def boot_sequence() -> None:
    steps = [
        "Initializing secure shell",
        "Mounting encrypted profile vault",
        "Loading command modules",
        "Syncing social endpoints",
        "Calibrating telemetry overlays",
        "Launching sanjjay dashboard",
    ]

    with Progress(
        SpinnerColumn(style="bright_black"),
        TextColumn("[grey82]{task.description}"),
        BarColumn(bar_width=34, complete_style="grey70", finished_style="white"),
        TextColumn("[grey58]{task.percentage:>3.0f}%"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("Booting...", total=len(steps))
        for step in steps:
            progress.update(task, description=step)
            time.sleep(0.25)
            progress.advance(task)

    console.print("[grey70]Boot complete.[/grey70] [bold white]Welcome, Sanjjay.[/bold white]\n")


def prompt_text() -> str:
    host = PROFILE["hostname"].split("@", 1)[-1]
    return f"[bold white]sanjjay[/bold white][grey50]@[/grey50][grey70]{host}[/grey70][grey50]:~$[/grey50] "


def fake_system_metrics(start_time: float) -> Table:
    uptime = int(time.time() - start_time)
    hours, rem = divmod(uptime, 3600)
    mins, secs = divmod(rem, 60)
    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column(style="grey70")
    table.add_column(style="white")
    table.add_row("status", "ONLINE")
    table.add_row("uptime", f"{hours:02d}:{mins:02d}:{secs:02d}")
    table.add_row("memory", f"{random.randint(34, 68)}%")
    table.add_row("cpu load", f"{random.randint(11, 53)}%")
    table.add_row("network", random.choice(["STABLE", "MONITORED", "SECURE"]))
    table.add_row("active modules", str(random.randint(7, 16)))
    table.add_row("last sync", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return table
