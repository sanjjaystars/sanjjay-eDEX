"""Main CLI entrypoint for sanjjay."""

from __future__ import annotations

import time

from rich.console import Console

from .commands import CommandHandler
from .ui import boot_sequence, prompt_text, render_banner, render_header

console = Console()


def run() -> None:
    """Run the interactive dashboard session."""
    start_time = time.time()
    boot_sequence()
    render_banner()
    render_header()

    handler = CommandHandler(start_time=start_time)

    while True:
        try:
            command = console.input(prompt_text())
        except (KeyboardInterrupt, EOFError):
            console.print("\n[grey70]Interrupt received.[/grey70]")
            command = "exit"

        should_continue = handler.execute(command.strip())
        if not should_continue:
            break


def main() -> None:
    """Console script entrypoint."""
    run()
